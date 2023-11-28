from rest_framework import generics
from ...models import User
from ..serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import Http404
from rest_framework import permissions

class UserListView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # @swagger_auto_schema(request_body=openapi.Schema(
    #     type=openapi.TYPE_OBJECT,
    #     properties={
    #         'email': openapi.Schema(type=openapi.TYPE_STRING, description="person email"),
    #         'password': openapi.Schema(type=openapi.TYPE_STRING, description="password person"),
    #     },
    #     required=['email', 'password'],
    # ))
    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter(
    #         in_= openapi.IN_QUERY,
    #         name= 'email',
    #         required=True,
    #         type=openapi.TYPE_STRING,
    #         description="email",
    #     )
    # ])
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)