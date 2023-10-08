from django.db import models
from django.utils.translation import gettext_lazy as _

class Rights(models.Model):
    can_ban = models.BooleanField(_('can ban'), default=False)
    can_kick = models.BooleanField(_('can kick'), default=False)