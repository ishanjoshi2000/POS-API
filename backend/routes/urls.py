from django.urls import path
from  .views import ProductListAPIView,CategoryListAPIView,ProductFilterAPIView
 
urlpatterns = [
            #Product Views
            path('products/',ProductListAPIView.as_view()),
            path('categories/',CategoryListAPIView.as_view()),
            path('products/filter/', ProductFilterAPIView.as_view())
]
