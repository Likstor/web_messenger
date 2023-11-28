from rest_framework import generics
from ...models import ServerUser, User, Server
from ..serializers import ServerUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
    
class ServerUserListView(APIView):
    queryset = ServerUser.objects.all()
    serializer_class = ServerUserSerializer
    
    def get(self, request, format=None):
        server_users = Server.objects.all()
        serializer = ServerUserSerializer(server_users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ServerUserSerializer)
    def post(self, request, format=None):
        serializer = ServerUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ServerUserDetailView(APIView):
    queryset = Server.objects.all()
    serializer_class = ServerUserSerializer

    def get_object(self, pk):
        try:
            return Server.objects.get(pk=pk)
        except Server.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        server_user = self.get_object(pk)
        serializer = ServerUserSerializer(server_user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        server_user = self.get_object(pk)
        serializer = ServerUserSerializer(server_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)