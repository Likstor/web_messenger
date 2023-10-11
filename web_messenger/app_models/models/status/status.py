from django.db import models
from django.utils.translation import gettext_lazy as _

class Status(models.Model):
    title = models.CharField(_('status title'), max_length=20)
    color = models.CharField(_('status color'))