
from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'id', 'name', 'description', 'price', 'stock']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ціна повинна бути додатною.")
        return value
    
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Кількість на складі не може бути від'ємною.")
        return value
    
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Назва продукту не може бути порожньою.")
        return value

class OrderItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='product.name', read_only=True)
    
    product_price = serializers.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        source='product.price', 
        read_only=True
    )

    # product = ProductSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['product_name', 'product_price', 'quantity', 'item_subtotal']


class OrderSerializer(serializers.ModelSerializer):
    
    items = OrderItemSerializer(many=True, read_only=True)

    total_price = serializers.SerializerMethodField(method_name='total')
    
    def total(self, obj):
        order_items = obj.items.all()
        total = sum(item.item_subtotal for item in order_items)
        return total
    
    class Meta:
        model = Order
        fields = ['order_id', 'created_at', 'user', 'status',   'items', 'total_price']