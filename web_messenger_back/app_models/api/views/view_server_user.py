from rest_framework import generics
from ...models import ServerUser, User, Server
from ..serializers import ServerUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

    
class ServerUserView(APIView):
    queryset = ServerUser.objects.all()
    serializer_class = ServerUserSerializer
    
    def get(self, request):
        server_users = ServerUser.objects.all()
        serializer = ServerUserSerializer(server_users, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ServerUserSerializer)   
    def post(self, request, format=None):
        serializer = ServerUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)