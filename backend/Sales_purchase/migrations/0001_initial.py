# Generated by Django 4.2.6 on 2024-08-11 12:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        ('LedgerAccounts', '0001_initial'),
        ('customers_vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NepaliCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gregorian_date', models.DateField(unique=True)),
                ('bs_year', models.IntegerField()),
                ('bs_month', models.IntegerField()),
                ('bs_day', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Nepali Calendar',
                'verbose_name_plural': 'Nepali Calendar',
                'unique_together': {('bs_year', 'bs_month', 'bs_day')},
            },
        ),
        migrations.CreateModel(
            name='PurchaseBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=20, unique=True)),
                ('bill_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('vat_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('taxable_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('non_taxable_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=20, unique=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers_vendors.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='SalesBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=20, unique=True)),
                ('bill_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('vat_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('taxable_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('non_taxable_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], max_length=20)),
                ('ref_bill_no', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers_vendors.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=20, unique=True)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers_vendors.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('vat_applicable', models.BooleanField(default=True)),
                ('vat_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vat_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.product')),
                ('sales_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales_purchase.salesorder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesBillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('vat_applicable', models.BooleanField(default=True)),
                ('vat_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vat_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.product')),
                ('sales_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales_purchase.salesbill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='salesbill',
            name='items',
            field=models.ManyToManyField(related_name='sales_bills', to='Sales_purchase.salesbillitem'),
        ),
        migrations.AddField(
            model_name='salesbill',
            name='order_bs_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Sales_purchase.nepalicalendar'),
        ),
        migrations.AddField(
            model_name='salesbill',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LedgerAccounts.paymentmode'),
        ),
        migrations.AddField(
            model_name='salesbill',
            name='sales_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sales_purchase.salesorder'),
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('vat_applicable', models.BooleanField(default=True)),
                ('vat_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vat_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.product')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales_purchase.purchaseorder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseBillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('vat_applicable', models.BooleanField(default=True)),
                ('vat_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vat_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.product')),
                ('purchase_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales_purchase.purchasebill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='items',
            field=models.ManyToManyField(related_name='purchase_bills', to='Sales_purchase.purchasebillitem'),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='order_bs_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Sales_purchase.nepalicalendar'),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LedgerAccounts.paymentmode'),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='purchase_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sales_purchase.purchaseorder'),
        ),
        migrations.AddField(
            model_name='purchasebill',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers_vendors.vendor'),
        ),
    ]