from rest_framework import serializers
from ..models import RightsServerUser, ServerUser

class RigthsServerUserSerializer(serializers.ModelField):
    class Meta:
        model = RightsServerUser
        fields = '__all__'


class ServerUserSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name')
    server = serializers.CharField(source='server.title')
    is_banned = serializers.BooleanField()
    data_banned = serializers.DateTimeField()
    is_muted = serializers.BooleanField()
    mute_time = serializers.TimeField()
    role = serializers.CharField(source='role.title')
    rights = RigthsServerUserSerializer()
    class Meta:
        model = ServerUser
        fields = ('user', 'server', 'is_banned',
                'data_banned', 'is_muted', 'mute_time',
                'rights', 'role')
        