from rest_framework import serializers
from ...models import ServerUser
from rest_framework.validators import UniqueTogetherValidator

class ServerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerUser
        fields = ('__all__')
        validators = [
            UniqueTogetherValidator(
                queryset=ServerUser.objects.all(),
                fields=['user', 'server']
            )
        ]