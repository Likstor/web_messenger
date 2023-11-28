from rest_framework import generics
from ...models import Rights
from ..serializers import RightsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
    
class RightsListView(APIView):
    queryset = Rights.objects.all()
    serializer_class = RightsSerializer
    
    def get(self, request, format=None):
        rights = Rights.objects.all()
        serializer = RightsSerializer(rights, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RightsSerializer)
    def post(self, request, format=None):
        serializer = RightsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RightsDetailView(APIView):
    queryset = Rights.objects.all()
    serializer_class = RightsSerializer

    def get_object(self, pk):
        try:
            return Rights.objects.get(pk=pk)
        except Rights.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        rights = self.get_object(pk)
        serializer = RightsSerializer(rights)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rights = self.get_object(pk)
        serializer = RightsSerializer(rights, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)