from django.db import models
from ..server.server import Server
from django.utils.translation import gettext_lazy as _

class Channel(models.Model):
    title = models.CharField(_('channel title'))
    server = models.ForeignKey(Server, on_delete=models.CASCADE)