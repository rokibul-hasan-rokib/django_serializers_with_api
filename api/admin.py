# api/admin.py

from django.contrib import admin
from .models import Custmer, Order

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'updated_at')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product_name', 'quantity', 'order_date')
    search_fields = ('product_name',)
    list_filter = ('order_date',)

admin.site.register(Custmer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)

