from rest_framework import serializers
from ...models import ChannelVoice

class ChannelVoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelVoice
        fields = ('__all__')