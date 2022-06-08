from django.contrib import admin
from .models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display=['size', 'order_status', 'quantity', 'created_at']
    list_filter=['created_at', 'order_status', 'size']