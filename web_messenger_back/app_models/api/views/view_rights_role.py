from rest_framework import generics
from ...models import RightsRole
from ..serializers import RightsRoleSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

    
class RightsRoleView(APIView):
    queryset = RightsRole.objects.all()
    serializer_class = RightsRoleSerializer
    
    def get(self, request):
        rights_roles = RightsRole.objects.all()
        serializer = RightsRoleSerializer(rights_roles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RightsRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)