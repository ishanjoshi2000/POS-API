from django.shortcuts import render
from django.http import Http404
from .models import Product
#ProductSerializers
# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product,Category,Vendor,Customer
from django.db.models import Q
from .serializers import ProductSerializer,CategorySerializer,CustomerSerializer
# Create your views here.

class CustomerDetailAPIView(APIView):
    def get_object(self, pan_no):
        try:
            return Customer.objects.get(pan_no=pan_no)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pan_no):
        customer = self.get_object(pan_no)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pan_no):
        customer = self.get_object(pan_no)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pan_no):
        customer = self.get_object(pan_no)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerListCreateAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)