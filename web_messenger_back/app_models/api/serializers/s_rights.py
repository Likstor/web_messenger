from rest_framework import serializers
from ...models import Rights

class RightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rights
        fields = ('__all__')