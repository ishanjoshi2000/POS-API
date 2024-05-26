# Generated by Django 4.2.6 on 2024-02-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_category_no_of_products_category_total_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buy_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='pan_no',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
