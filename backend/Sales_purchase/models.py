from django.db import models
from django.utils import timezone
from Products.models import Product  
from customers_vendors.models import Customer, Vendor  
from LedgerAccounts.models import Ledger,PaymentMode  
from django.db import models

class NepaliCalendar(models.Model):
    gregorian_date = models.DateField(unique=True)
    bs_year = models.IntegerField()
    bs_month = models.IntegerField()
    bs_day = models.IntegerField()

    def __str__(self):
        return f"{self.bs_year}-{self.bs_month:02d}-{self.bs_day:02d} (BS)"

    class Meta:
        unique_together = ('bs_year', 'bs_month', 'bs_day')
        verbose_name = "Nepali Calendar"
        verbose_name_plural = "Nepali Calendar"

class AbstractBill(models.Model):
    bill_no = models.CharField(max_length=20, unique=True)
    bill_date = models.DateTimeField(default=timezone.now)
    order_bs_date = models.ForeignKey('NepaliCalendar', on_delete=models.PROTECT)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    taxable_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    non_taxable_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ])

    class Meta:
        abstract = True

    def calculate_totals(self):
        self.vat_amount = sum(item.calculate_vat_amount() for item in self.items.all())
        self.discount_amount = sum(item.calculate_discount_amount() for item in self.items.all())
        self.taxable_amount = sum(item.calculate_taxable_amount() for item in self.items.all())
        self.non_taxable_amount = sum(item.calculate_non_taxable_amount() for item in self.items.all())
        self.total_amount = self.taxable_amount + self.vat_amount - self.discount_amount

    def save(self, *args, **kwargs):
        self.calculate_totals()
        super().save(*args, **kwargs)

class OrderItemMixin(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    vat_applicable = models.BooleanField(default=True)
    vat_rate = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        abstract = True

    def calculate_vat_amount(self):
        if self.vat_applicable and self.vat_rate:
            return (self.price * self.quantity) * (self.vat_rate / 100)
        return 0

    def calculate_discount_amount(self):
        if self.discount:
            return (self.price * self.quantity) * (self.discount / 100)
        return 0

    def calculate_total_amount(self):
        return (self.price * self.quantity) + self.calculate_vat_amount() - self.calculate_discount_amount()

class SalesOrder(models.Model):
    order_no = models.CharField(max_length=20, unique=True)
    order_date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Sales Order {self.order_no}"

class PurchaseOrder(models.Model):
    order_no = models.CharField(max_length=20, unique=True)
    order_date = models.DateTimeField(default=timezone.now)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Purchase Order {self.order_no}"

class SalesOrderItem(OrderItemMixin, models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.vat_amount = self.calculate_vat_amount()
        self.discount_amount = self.calculate_discount_amount()
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.sales_order.order_no}"

class PurchaseOrderItem(OrderItemMixin, models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.vat_amount = self.calculate_vat_amount()
        self.discount_amount = self.calculate_discount_amount()
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.purchase_order.order_no}"

class SalesBill(AbstractBill):
    payment_method = models.ForeignKey(PaymentMode, on_delete=models.PROTECT)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField('SalesBillItem', related_name='sales_bills')
    ref_bill_no = models.CharField(max_length=20, unique=True, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)  
    def save(self, *args, **kwargs):
        if self.sales_order and not self.ref_bill_no:
            self.ref_bill_no = self.sales_order.order_no
        super().save(*args, **kwargs)

class PurchaseBill(AbstractBill):
    payment_method = models.ForeignKey(PaymentMode, on_delete=models.PROTECT)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField('PurchaseBillItem', related_name='purchase_bills')
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)  

class SalesBillItem(OrderItemMixin, models.Model):
    sales_bill = models.ForeignKey(SalesBill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.vat_amount = self.calculate_vat_amount()
        self.discount_amount = self.calculate_discount_amount()
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.sales_bill.bill_no}"

class PurchaseBillItem(OrderItemMixin, models.Model):
    purchase_bill = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.vat_amount = self.calculate_vat_amount()
        self.discount_amount = self.calculate_discount_amount()
        self.total_amount = self.calculate_total_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.purchase_bill.bill_no}"
