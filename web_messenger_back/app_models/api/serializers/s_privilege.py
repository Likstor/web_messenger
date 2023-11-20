from rest_framework import serializers
from ...models import Privilege
from rest_framework.validators import UniqueTogetherValidator

class PrivilegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privilege
        fields = ('__all__')
        validators = [
            UniqueTogetherValidator(
                queryset=Privilege.objects.all(),
                fields=['serveruser', 'channel']
            )
        ]