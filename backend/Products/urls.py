from django.urls import path
from  .views import ProductListAPIView,CategoryListAPIView,ProductFilterAPIView,CustomerDetailAPIView,CustomerListCreateAPIView
 
urlpatterns = [
            #Product Views
            path('products/',ProductListAPIView.as_view()),
            path('categories/',CategoryListAPIView.as_view()),
            path('products/filter/', ProductFilterAPIView.as_view()),
            path('customers/', CustomerListCreateAPIView.as_view()),
            path('customers/<str:pan_no>/', CustomerDetailAPIView.as_view())
]
