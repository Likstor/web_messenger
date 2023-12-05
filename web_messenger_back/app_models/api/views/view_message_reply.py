from rest_framework import generics
from ...models import MessageReply
from ..serializers import MessageReplySerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
from drf_yasg import openapi
    
class MessageReplyListView(APIView):
    queryset = MessageReply.objects.all()
    serializer_class = MessageReplySerializer
    
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            name='user',
            in_=openapi.IN_QUERY,
            description="messages of person",
            type=openapi.TYPE_STRING,
        )
    ])
    def get(self, request, format=None):
        if request.query_params:
            message_replies = MessageReply.objects.filter(user=request.GET.get('user'))
        else:
            message_replies = MessageReply.objects.all()
        serializer = MessageReplySerializer(message_replies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MessageReplySerializer)
    def post(self, request, format=None):
        serializer = MessageReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MessageReplyDetailView(APIView):
    queryset = MessageReply.objects.all()
    serializer_class = MessageReplySerializer

    def get_object(self, pk):
        try:
            return MessageReply.objects.get(pk=pk)
        except MessageReply.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        message_reply = self.get_object(pk)
        serializer = MessageReplySerializer(message_reply)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        message_reply = self.get_object(pk)
        serializer = MessageReplySerializer(message_reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        message_reply = self.get_object(pk)
        message_reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)