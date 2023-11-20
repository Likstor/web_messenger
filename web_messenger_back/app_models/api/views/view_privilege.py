from rest_framework import generics
from ...models import Privilege
from ..serializers import PrivilegeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

    
class PrivilegeView(APIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer
    
    def get(self, request):
        privilegies = Privilege.objects.all()
        serializer = PrivilegeSerializer(privilegies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PrivilegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)