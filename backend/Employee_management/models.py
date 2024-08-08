from django.db import models
from django.core.exceptions import ValidationError

def validate_employee_id(value):
    if not value.isdigit() or len(value) != 6:
        raise ValidationError('Employee ID must be exactly 6 digits long.')

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_id = models.CharField(max_length=6, unique=True, validators=[validate_employee_id])
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
