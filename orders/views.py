from signal import set_wakeup_fd
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from . import serializers
from .models import Orders

User=get_user_model()

class OrderCreateListView(generics.GenericAPIView):
    serializer_class=serializers.OrderCreationSerializer
    queryset=Orders.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary='Get the list of all orders')
    def get(self, request):
        orders=Orders.objects.all()
        serializer=self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary='Make an order')
    def post(self, request):
        data=request.data
        serializer=self.serializer_class(data=data)
        user=request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):

    serializer_class=serializers.OrderDetailSerializer
    permission_classes=[IsAdminUser]

    @swagger_auto_schema(operation_summary='Get the details of a specific order')
    def get(self, request, order_id):
        order=get_object_or_404(Orders, pk=order_id)
        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary='Edit the details of an order')
    def put(self, request, order_id):
        data=request.data

        order=get_object_or_404(Orders, pk=order_id)

        serializer=self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Delete an order')
    def delete(self, request, order_id):
        order=get_object_or_404(Orders, pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateOrderStatus(generics.GenericAPIView):
    
    serializer_class=serializers.UpdateOrderSerializer
    permission_classes=[IsAdminUser]

    @swagger_auto_schema(operation_summary='Update/Edit the status of an order')
    def put(self, request, order_id):
        
        order=get_object_or_404(Orders, pk=order_id)

        data=request.data

        serializer=self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserOrdersView(generics.GenericAPIView):

    serializer_class=serializers.OrderDetailSerializer

    @swagger_auto_schema(operation_summary='Get all orders from a specific user')
    def get(self, request, user_id):

        user=User.objects.get(pk=user_id)

        orders=Orders.objects.all().filter(customer=user)

        serializer=self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data)

class UserOrderDetail(generics.GenericAPIView):

    serializer_class=serializers.OrderDetailSerializer

    @swagger_auto_schema(operation_summary='Get details for a specific order from a specific user')
    def get(self, request, user_id, order_id):
        user=User.objects.get(pk=user_id)
        order=Orders.objects.all().filter(customer=user).get(pk=order_id)

        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
