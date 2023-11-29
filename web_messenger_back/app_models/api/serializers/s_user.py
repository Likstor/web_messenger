from rest_framework import serializers
from ...models import User

class PatchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'description', 'status_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')