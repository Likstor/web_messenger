from rest_framework import generics
from ...models import Role
from ..serializers import RoleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
from drf_yasg import openapi
    
class RoleListView(APIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            name='server',
            description='roles from server',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        )
    ])
    def get(self, request, format=None):
        if (request.query_params):
            roles = Role.objects.filter(server=request.GET.get('server'))
        else:
            roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RoleSerializer)
    def post(self, request, format=None):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoleDetailView(APIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_object(self, pk):
        try:
            return Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        role = self.get_object(pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)