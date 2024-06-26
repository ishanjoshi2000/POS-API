# Generated by Django 4.2.6 on 2023-10-28 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_category_alter_product_options_remove_customer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='no_of_products',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='total_sales',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
