from django.http import Http404
from .models import Product
#ProductSerializers
# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product,Category
from django.db.models import Q
from .serializers import ProductSerializer,CategorySerializer

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductFilterAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        category = request.query_params.get('category', '')
        page = int(request.query_params.get('page', 1))
        page_size = 28
        
        filters = Q()
        if query:
            filters &= Q(name__icontains=query)
        if category:
            filters &= Q(category__name=category)
        
        products = Product.objects.filter(filters)
        total_products = products.count()
        
        start = (page - 1) * page_size
        end = start + page_size
        
        products = products[start:end]
        
        serializer = ProductSerializer(products, many=True)
        
        return Response({
            'products': serializer.data,
            'total_products': total_products,
            'page': page,
            'page_size': page_size,
        })

class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    #VendorSerializers
    '''
class VendorCreateView(CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorUpdateView(UpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class GetVendorByIdView(RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class DeleteVendorView(DestroyAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer
#Customer  Serializers
class CustomerCreateView(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
'''