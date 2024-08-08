from django.contrib import admin
from .import models

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=['name','sell_price']
    list_editable=['sell_price']
    list_per_page=15
    ordering=['name']
    search_fields=['name__istartswith']
    exclude = ('units_sold', 'stock_in_hand')
class CategoryAdmin(admin.ModelAdmin):
  exclude = ('no_of_products','total_sales')

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Product,productAdmin)



