from django.db import models
from ..message.message import Message

class MessageReply(Message):
    reply = models.ForeignKey(Message, on_delete=models.CASCADE)