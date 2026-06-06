from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Product, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Адмін панель для моделі Product.
    """
    list_display = ['name', 'price', 'stock', 'in_stock']
    list_filter = ['stock']
    search_fields = ['name', 'description']
    readonly_fields = ['in_stock']


class OrderItemInline(admin.TabularInline):
    """
    Inline для відображення OrderItem в Order.
    """
    model = OrderItem
    extra = 1
    readonly_fields = ['item_subtotal']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Адмін панель для моделі Order.
    """
    list_display = ['order_id', 'user', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_id', 'user__username']
    readonly_fields = ['order_id', 'created_at']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Адмін панель для моделі OrderItem.
    """
    list_display = ['order', 'product', 'quantity', 'item_subtotal']
    list_filter = ['order__status']
    readonly_fields = ['item_subtotal']


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Адмін панель для моделі User.
    """
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']