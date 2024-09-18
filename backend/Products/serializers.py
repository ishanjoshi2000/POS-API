from rest_framework import serializers 
from Products.models import Product,Category,ProductUnit,Unit

class ProductUnitSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = ProductUnit
        fields = ['id', 'product', 'unit', 'conversion_rate', 'image', 'alternate_price', 'display_name']

    def get_display_name(self, obj):
        return f"{obj.product.name} - ({obj.unit.name})"
    
class ProductSerializer(serializers.ModelSerializer):
    product_units = ProductUnitSerializer(many=True)  
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'base_unit', 'price', 'image', 'product_units']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']