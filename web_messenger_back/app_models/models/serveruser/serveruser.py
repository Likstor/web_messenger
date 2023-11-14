from django.db import models
from django.utils.translation import gettext_lazy as _
from ..user.user import User
from ..server.server import Server
from ..rights import RightsServerUser
from ..role.role import Role
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import ServerUserSerializer


class ServerUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True)
    username_local = models.CharField(_('username local'), max_length=30, null=True, blank=True)
    is_banned = models.BooleanField(_('is banned'), default=False)
    data_banned = models.DateTimeField(_('date banned'), null=True, blank=True)
    is_muted = models.BooleanField(_('is muted'), default=False)
    mute_time = models.TimeField(_('mute time'), null=True, blank=True)
    rights = models.OneToOneField(RightsServerUser, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username_local
    
# class GetServerUserInfo(APIView):
#     def get(self, request):
#         queryset = ServerUser.objects.all()
#         serializer_for_queryset = ServerUserSerializer(
#             instance=queryset,
#             many=True
#         )
#         return Response(serializer_for_queryset.data)
    
