from rest_framework import serializers
from ...models import RightsRole

class RightsRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RightsRole
        fields = ('__all__')