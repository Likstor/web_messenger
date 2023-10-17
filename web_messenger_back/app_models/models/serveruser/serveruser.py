from django.db import models
from django.utils.translation import gettext_lazy as _
from ..user.user import User
from ..server.server import Server
from ..rights import RightsServerUser
from ..role.role import Role


class ServerUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, null=True)
    username_local = models.CharField(_('username local'), max_length=30, null=True)
    is_banned = models.BooleanField(_('is banned'), default=False)
    data_banned = models.DateTimeField(_('date banned'), null=True)
    is_muted = models.BooleanField(_('is muted'), default=False)
    mute_time = models.TimeField(_('mute time'), null=True)
    rights = models.OneToOneField(RightsServerUser, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username_local