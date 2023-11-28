from rest_framework import generics
from ...models import ChannelVoice
from ..serializers import ChannelVoiceSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
    
class ChannelVoiceView(APIView):
    queryset = ChannelVoice.objects.all()
    serializer_class = ChannelVoiceSerializer
    
    def get(self, request):
        channel_voices = ChannelVoice.objects.all()
        serializer = ChannelVoiceSerializer(channel_voices, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=ChannelVoiceSerializer)    
    def post(self, request, format=None):
        serializer = ChannelVoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)