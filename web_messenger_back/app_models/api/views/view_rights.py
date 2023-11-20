from rest_framework import generics
from ...models import Rights
from ..serializers import RightsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

    
class RightsView(APIView):
    queryset = Rights.objects.all()
    serializer_class = RightsSerializer
    
    def get(self, request):
        rights = Rights.objects.all()
        serializer = RightsSerializer(rights, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RightsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)