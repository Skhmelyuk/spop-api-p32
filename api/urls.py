from django.urls import path
from . import views
from .views import ProductUpdateDestroyDetailAPI, ProductListCreateApi, OrderAPIList

app_name = 'api'

urlpatterns = [
    path('products/', ProductListCreateApi.as_view(), name='product_list_create'),
    path('products/<int:pk>/', ProductUpdateDestroyDetailAPI.as_view(), name='product_detail'),
    path('orders/', OrderAPIList.as_view(), name='order_list'),
]