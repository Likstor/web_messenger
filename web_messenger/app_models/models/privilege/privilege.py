from django.db import models
from django.utils.translation import gettext_lazy as _
from ..role.role import Role
from ..serveruser.serveruser import ServerUser
from ..channel.channel import Channel

class Privilege(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    serveruser = models.ForeignKey(ServerUser, on_delete=models.CASCADE, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)