from rest_framework import generics
from ...models import ChannelText, Server
from ..serializers import ChannelTextSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

    
class ChannelTextView(APIView):
    queryset = ChannelText.objects.all()
    serializer_class = ChannelTextSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        channel_texts = ChannelText.objects.all()
        serializer = ChannelTextSerializer(channel_texts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = ChannelTextSerializer(data=request.data)
        
        if not request.user.id == Server.objects.get(pk=request.data['server']).owner.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)