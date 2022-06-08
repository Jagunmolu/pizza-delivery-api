from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from . import serializers
from authentication import serializers
from rest_framework.permissions import IsAdminUser

class NewAuthView(generics.GenericAPIView):

    def get(self, request):
        return Response(data={'message':'You are an amazing developer!'})


class UserCreateView(generics.GenericAPIView):

    serializer_class=serializers.UserCreationSerializer
    permission_classes=[IsAdminUser]

    @swagger_auto_schema(operation_summary='Create a User account')
    def post(self, request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)