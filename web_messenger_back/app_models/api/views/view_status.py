from rest_framework import generics
from ...models import Status
from ..serializers import StatusSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

class StatusListView(APIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    def get(self, request, format=None):
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StatusSerializer)
    def post(self, request, format=None):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StatusDetailView(APIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_object(self, pk):
        try:
            return Status.objects.get(pk=pk)
        except Status.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        status = self.get_object(pk)
        serializer = StatusSerializer(status)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=StatusSerializer)
    def put(self, request, pk, format=None):
        status = self.get_object(pk)
        serializer = StatusSerializer(status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        status = self.get_object(pk)
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
