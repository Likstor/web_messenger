from rest_framework import serializers
from ...models import ChannelText

class ChannelTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelText
        fields = ('__all__')