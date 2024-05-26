from rest_framework import serializers 
from routes.models import Product,Vendor,Customer,Category
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ['id','name', 'sell_price', 'image', 'category']

class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'sell_price', 'image', 'category']
  
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

    def validate_pan_no(self, value):
        if value and len(value) > 9:
            raise serializers.ValidationError("PAN number cannot exceed 9 characters.")
        return value
    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'address', 'pan_no', 'membership']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

