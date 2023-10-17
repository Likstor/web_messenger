from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'phone', 'date_joined', 'is_banned', 'date_banned', 'is_active', 'is_staff', 'status_id', 'avatar')
    list_filter = ('date_joined', 'date_banned', 'is_staff')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('time', 'user', 'text', 'file', 'text_channel')
    list_filter = ('time',)


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('title', 'server')


class ChannelTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'server')


class ChannelVoiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'server')


class PrivilegeAdmin(admin.ModelAdmin):
    list_display = ('role', 'serveruser', 'channel')


class RightsRoleAdmin(admin.ModelAdmin):
    list_display = ('can_ban', 'can_kick')



admin.site.register(Channel, ChannelAdmin)
admin.site.register(ChannelText, ChannelTextAdmin)
admin.site.register(ChannelVoice, ChannelVoiceAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Privilege, PrivilegeAdmin)
admin.site.register(Role)
admin.site.register(Server)
admin.site.register(ServerUser)
admin.site.register(Status)
admin.site.register(User, UserAdmin)
admin.site.register(Rights)
admin.site.register(RightsRole, RightsRoleAdmin)
admin.site.register(RightsServerUser)