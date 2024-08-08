from django.db import models
from django.core.exceptions import ValidationError

def validate_pan_no(value):
    if not value.isdigit() or len(value) != 9:
        raise ValidationError('PAN number must be exactly 9 digits long.')

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pan_no = models.CharField(max_length=9, validators=[validate_pan_no])
    due_days = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Customer(models.Model):
    MEMBERSHIP_CHOICES = [
        ('ORDINARY', 'Ordinary'),
        ('REGULAR', 'Regular'),
        ('SPECIAL', 'Special'),
    ]

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pan_no = models.CharField(max_length=9, validators=[validate_pan_no])
    due_days = models.PositiveIntegerField(default=0)
    membership = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='ORDINARY')

    def __str__(self):
        return self.name
    