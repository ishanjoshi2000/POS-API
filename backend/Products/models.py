from django.db import models
from django.core.exceptions import ValidationError
import random

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    no_of_products = models.PositiveIntegerField(default=0)
    total_sales = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

def validate_product_code(value):
    if not value.isalnum() or len(value) != 6:
        raise ValidationError('Product code must be exactly 6 alphanumeric characters.')
    
class Product(models.Model):
    product_code = models.CharField(max_length=6, unique=True, validators=[validate_product_code], editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    base_unit = models.ForeignKey(Unit, related_name='base_unit', on_delete=models.SET_NULL, null=True)
    alternate_units = models.ManyToManyField(Unit, through='ProductUnit')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vat_applicable = models.BooleanField(default=False)
    vat_rate = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    stock_quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.product_code})"

    def save(self, *args, **kwargs):
        if not self.product_code:
            self.product_code = self.generate_product_code()
        super().save(*args, **kwargs)

    def generate_product_code(self):
        initials = ''.join([word[0] for word in self.name.split()][:2]).upper()
        while True:
            random_number = str(random.randint(1000, 9999))  # Always 4 digits
            code = f"{initials}{random_number}"
            if not Product.objects.filter(product_code=code).exists():
                return code
            
class AlternateUnit(models.Model):
    product = models.ForeignKey(Product, related_name='alternate_units', on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=50)
    conversion_rate = models.PositiveIntegerField()  

    def __str__(self):
        return f"{self.unit_name} ({self.conversion_rate} {self.product.base_unit})"


