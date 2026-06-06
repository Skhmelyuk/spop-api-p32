from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework import generics


# get all products and create new product
class ProductListCreateApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# get product by id and update and delete product
class ProductUpdateDestroyDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# get all orders
class OrderAPIList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer