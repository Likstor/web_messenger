from rest_framework import generics
from ...models import MessageReply
from ..serializers import MessageReplySerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

    
class MessageReplyView(APIView):
    queryset = MessageReply.objects.all()
    serializer_class = MessageReplySerializer
    
    def get(self, request):
        message_replies = MessageReply.objects.all()
        serializer = MessageReplySerializer(message_replies, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MessageReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)