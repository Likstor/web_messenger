from rest_framework import generics
from ...models import Privilege
from ..serializers import PrivilegeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
    
class PrivilegeListView(APIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer
    
    def get(self, request, format=None):
        privilegies = Privilege.objects.all()
        serializer = PrivilegeSerializer(privilegies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PrivilegeSerializer)
    def post(self, request, format=None):
        serializer = PrivilegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PrivilegeDetailView(APIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer

    def get_object(self, pk):
        try:
            return Privilege.objects.get(pk=pk)
        except Privilege.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        privilege = self.get_object(pk)
        serializer = PrivilegeSerializer(privilege)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        privilege = self.get_object(pk)
        serializer = PrivilegeSerializer(privilege, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)