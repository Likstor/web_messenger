from rest_framework import serializers
from ...models import RightsServerUser

class RightsServerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RightsServerUser
        fields = ('__all__')