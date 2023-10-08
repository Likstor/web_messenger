from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(Privilege)
admin.site.register(Role)
admin.site.register(Server)
admin.site.register(ServerUser)
admin.site.register(Status)
admin.site.register(User)
admin.site.register(Rights)
admin.site.register(RightsRole)
admin.site.register(RightsServerUser)