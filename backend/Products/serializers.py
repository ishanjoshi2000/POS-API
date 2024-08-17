from rest_framework import serializers 
from Products.models import Product,Category


class ProductDisplaySerializer(serializers.ModelSerializer):
    class meta:
        model=Product
        feilds=['id','name','category','base_unit','price','image']