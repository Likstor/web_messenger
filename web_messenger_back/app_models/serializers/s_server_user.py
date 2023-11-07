from rest_framework import serializers
from ..models import *


class ServerUserSerializer(serializers.Serializer):
    user = serializers.CharField(source='user.user_name')
    server = serializers.CharField(source='server.title')
    is_banned = serializers.BooleanField()
    data_banned = serializers.DateTimeField()
    is_muted = serializers.BooleanField()
    mute_time = serializers.TimeField()
    role = serializers.CharField(source='role.title')
    class Meta:
        model = RightsServerUser
        fields = ('user', 'server', 'is_banned',
                  'data_banned', 'is_muted', 'mute_time',
                  'can_ban', 'can_kick', 'role')