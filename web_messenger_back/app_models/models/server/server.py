from django.db import models
from ..user.user import User
from django.utils.translation import gettext_lazy as _

class Server(models.Model):
    title = models.CharField(_('server title'))
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title} | {self.id}'