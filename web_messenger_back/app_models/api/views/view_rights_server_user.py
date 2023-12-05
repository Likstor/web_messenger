from rest_framework import generics
from ...models import RightsServerUser
from ..serializers import RightsServerUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404
    
class RightsServerUserListView(APIView):
    queryset = RightsServerUser.objects.all()
    serializer_class = RightsServerUserSerializer
    
    def get(self, request, format=None):
        rights_server_users = RightsServerUser.objects.all()
        serializer = RightsServerUserSerializer(rights_server_users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RightsServerUserSerializer)
    def post(self, request, format=None):
        serializer = RightsServerUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RightsServerUserDetailView(APIView):
    queryset = RightsServerUser.objects.all()
    serializer_class = RightsServerUserSerializer

    def get_object(self, pk):
        try:
            return RightsServerUser.objects.get(pk=pk)
        except RightsServerUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        rights_server_user = self.get_object(pk)
        serializer = RightsServerUserSerializer(rights_server_user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rights_server_user = self.get_object(pk)
        serializer = RightsServerUserSerializer(rights_server_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        rights_server_user = self.get_object(pk)
        rights_server_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)