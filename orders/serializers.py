from rest_framework import serializers

from .models import Orders


class OrderCreationSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=20)
    order_status=serializers.HiddenField(default='PENDING')
    quantity=serializers.IntegerField()

    class Meta:
        model=Orders
        fields=('size', 'order_status', 'quantity', 'id',)


class OrderDetailSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=20)
    order_status=serializers.CharField(default='PENDING')
    quantity=serializers.IntegerField()
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()

    class Meta:
        model=Orders
        fields=('id', 'size', 'order_status', 'quantity', 'created_at', 'updated_at',)

class UpdateOrderSerializer(serializers.ModelSerializer):
    order_status=serializers.CharField(default='PENDING')

    class Meta:
        model=Orders
        fields=('size', 'order_status', 'quantity', 'created_at', 'updated_at',)

