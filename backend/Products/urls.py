from django.urls import path,include
from .views import ProductViewSet,UnitViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'Units',UnitViewSet,basename='units')
urlpatterns = [
             path('', include(router.urls)),           
]
