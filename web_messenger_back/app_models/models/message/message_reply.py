from django.db import models
from ..message.message import Message

class MessageReply(Message):
    answer_to = models.ForeignKey(Message,related_name="message_reply", on_delete=models.DO_NOTHING)