import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'general.settings'

from rest_framework import renderers, serializers
from django import setup
setup()

from app_models.models import Role, User, Server, Rights
from app_models.serializers import ServerUserSerializer

class ServerUser:
    def __init__(self, user: User, server: Server, role: Role, rights: Rights):
        self.user = user
        self.server = server
        self.role = role
        self.rights = rights

user = User()
user.user_name = "duck"
server = Server()
role = Role()
rights = Rights()
serveruser = ServerUser(user, server, role, rights)

queryset = [serveruser]

serializer_obj = ServerUserSerializer(instance=queryset, many=True)

jsonrender = renderers.JSONRenderer()
data_is_json = jsonrender.render(serializer_obj.data)

