from rest_framework import generics
from ...models import Channel
from ..serializers import ChannelSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
from drf_yasg import openapi  

class ChannelListView(APIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            name='server',
            in_=openapi.IN_QUERY,
            description="channels of server",
            type=openapi.TYPE_STRING,
        )
    ])
    def get(self, request, format=None):
        if request.query_params:
            channels = Channel.objects.filter(server=request.GET.get('server'))
        else:
            channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ChannelSerializer)
    def post(self, request, format=None):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChannelDetailView(APIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get_object(self, pk):
        try:
            return Channel.objects.get(pk=pk)
        except Channel.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        channel = self.get_object(pk)
        serializer = ChannelSerializer(channel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        channel = self.get_object(pk)
        serializer = ChannelSerializer(channel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        channel = self.get_object(pk)
        channel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)