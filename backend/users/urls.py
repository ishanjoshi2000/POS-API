from django.urls import path
from .views import LoginView, UserList, UserDetail

urlpatterns = [
    # URL for user authentication
    path('login/', LoginView.as_view(), name='login'),

    # URLs for user CRUD operations
    path('userlist/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]