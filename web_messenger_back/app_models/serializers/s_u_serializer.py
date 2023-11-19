from rest_framework import serializers
from ..models import RightsServerUser, ServerUser


class ServerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerUser
        fields = ('__all__')
        