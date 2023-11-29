from rest_framework import generics
from ...models import ServerUser, User, Server
from ..serializers import ServerUserSerializer, PatchServerUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from django.http import Http404
    
class ServerUserListView(APIView):
    queryset = ServerUser.objects.all()
    serializer_class = ServerUserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            in_=openapi.IN_QUERY,
            name='server',
            description='persons from server',
            type=openapi.TYPE_STRING,
        )
    ])
    def get(self, request, format=None):
        if (request.query_params):
            server_users = ServerUser.objects.filter(server=request.GET.get('server'))
        else:
            server_users = ServerUser.objects.all()
        serializer = ServerUserSerializer(server_users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ServerUserSerializer)
    def post(self, request, format=None):
        request.data['username_local'] = request.user.user_name
        request.data['user'] = request.user.id
        serializer = ServerUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ServerUserDetailView(APIView):
    queryset = ServerUser.objects.all()
    serializer_class = ServerUserSerializer

    def get_object(self, pk):
        try:
            return ServerUser.objects.get(pk=pk)
        except ServerUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        server_user = self.get_object(pk)
        serializer = ServerUserSerializer(server_user)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ServerUserSerializer)
    def put(self, request, pk, format=None):
        server_user = self.get_object(pk)
        serializer = ServerUserSerializer(server_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=PatchServerUserSerializer)
    def patch(self, request, pk, format=None):
        server_user = self.get_object(pk)
        serializer = PatchServerUserSerializer(server_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        server_user = self.get_object(pk)
        server_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)