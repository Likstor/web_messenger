from app_models.serializers import ServerUserSerializer
from app_models.models import ServerUser
from rest_framework.views import APIView
from rest_framework.response import Response

class ServerUserInfo(APIView):
    serializer_class = ServerUserSerializer
    model = ServerUser
    def post(self, request):
        serializer_for_server_user = self.serializer_class(data=request.data)
        serializer_for_server_user.is_valid(raise_exception=True)
        serializer_for_server_user.save()
        return Response(data=serializer_for_server_user.data)