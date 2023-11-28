from rest_framework import generics
from ...models import Server, ServerUser
from ..serializers import ServerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404

class ServerListView(APIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        users = Server.objects.all()
        serializer = ServerSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ServerSerializer)
    def post(self, request, format=None):
        request.data['owner'] = request.user.id
        serializer = ServerSerializer(data=request.data)
        serializer.owner = request.user.id
        if serializer.is_valid():
            serializer.save()
            
            server = Server.objects.filter(owner=request.user.id).latest('id')
            
            serveruser = ServerUser(user=request.user, username_local=request.user.user_name, server=server);
            serveruser.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ServerDetailView(APIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def get_object(self, pk):
        try:
            return Server.objects.get(pk=pk)
        except Server.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ServerSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ServerSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)