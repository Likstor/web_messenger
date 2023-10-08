from django.db import models
from ..channel.text_channel import TextChannel
from ..user.user import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Message(models.Model):
    text_channel = models.ForeignKey(TextChannel, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(_('text in message'), null=True)
    file = models.FileField(_('file that will send'), upload_to='files/user_files', null=True)
    time = models.DateTimeField(_('message time'), default=timezone.now)
