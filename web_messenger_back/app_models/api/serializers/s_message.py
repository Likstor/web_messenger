from rest_framework import serializers
from ...models import MessageReply

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageReply
        fields = ('__all__')