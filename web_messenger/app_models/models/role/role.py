from django.db import models
from ..server.server import Server
from django.utils.translation import gettext_lazy as _
from ..rights.rights_role import RightsRole

class Role(models.Model):
    title = models.CharField(_('role title'), max_length=20)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    color = models.CharField()
    role_rights = models.OneToOneField(
        RightsRole,
        on_delete=models.CASCADE
    )
