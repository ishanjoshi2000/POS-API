from django.db import models

# Create your models here.

class Ledger(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('cash', 'Cash'),
        ('bank', 'Bank Account'),
        ('online', 'Online Payment'),
    ]
    
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    account_number = models.CharField(max_length=50, blank=True, null=True)  
    bank_name = models.CharField(max_length=100, blank=True, null=True) 
    online_provider = models.CharField(max_length=100, blank=True, null=True)  
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.account_type})"
    
class PaymentMode(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    associated_to=models.ForeignKey(Ledger, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name
    

