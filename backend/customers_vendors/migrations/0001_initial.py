# Generated by Django 4.2.6 on 2024-08-11 12:20

import customers_vendors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pan_no', models.CharField(max_length=9, validators=[customers_vendors.models.validate_pan_no])),
                ('due_days', models.PositiveIntegerField(default=0)),
                ('membership', models.CharField(choices=[('ORDINARY', 'Ordinary'), ('REGULAR', 'Regular'), ('SPECIAL', 'Special')], default='ORDINARY', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pan_no', models.CharField(max_length=9, validators=[customers_vendors.models.validate_pan_no])),
                ('due_days', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]