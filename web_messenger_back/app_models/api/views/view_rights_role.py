from rest_framework import generics
from ...models import RightsRole
from ..serializers import RightsRoleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
    
class RightsRoleListView(APIView):
    queryset = RightsRole.objects.all()
    serializer_class = RightsRoleSerializer
    
    def get(self, request, format=None):
        rights_roles = RightsRole.objects.all()
        serializer = RightsRoleSerializer(rights_roles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RightsRoleSerializer)
    def post(self, request, format=None):
        serializer = RightsRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RightsRoleDetailView(APIView):
    queryset = RightsRole.objects.all()
    serializer_class = RightsRoleSerializer

    def get_object(self, pk):
        try:
            return RightsRole.objects.get(pk=pk)
        except RightsRole.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        rights_role = self.get_object(pk)
        serializer = RightsRoleSerializer(rights_role)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rights_role = self.get_object(pk)
        serializer = RightsRoleSerializer(rights_role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        rights_role = self.get_object(pk)
        rights_role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)