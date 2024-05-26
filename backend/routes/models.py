from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    no_of_products = models.PositiveIntegerField(default=0)
    total_sales = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    units_sold = models.PositiveIntegerField(default=0)
    stock_in_hand = models.PositiveIntegerField(default=0)
    image=models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=None)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']
       

class SalesOrder(models.Model):
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
    
    
class PurchaseOrder(models.Model):
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    vendor_name = models.CharField(max_length=255)  # Vendor name for the purchase order
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Customer(models.Model):
    MEMBERSHIP_CHOICES = (
        ('ordinary', 'Ordinary'),
        ('regular', 'Regular'),
        ('special', 'Special'),
    )    
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    pan_no = models.CharField(max_length=20,primary_key=True)
    membership=models.CharField(max_length=100, choices=MEMBERSHIP_CHOICES, unique=True)
    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=200,)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    pan_no = models.CharField(max_length=9, unique=True)    
    def __str__(self):
        return self.name

