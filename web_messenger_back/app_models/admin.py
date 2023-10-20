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


class ServerAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
    list_filter = ('owner',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'color', 'server', 'role_rights')
    list_filter = ('server',)


class ServerUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'username_local', 'server', 'is_banned', 'data_banned', 'is_muted', 'mute_time', 'role', 'rights')
    list_filter = ('is_banned', 'is_muted', 'role')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('title', 'color')


class RightsAdmin(admin.ModelAdmin):
    list_display = ('can_ban', 'can_kick')


class RightsServerUserAdmin(admin.ModelAdmin):
    list_display = ('can_ban', 'can_kick')


class MessageReplyAdmin(admin.ModelAdmin):
    list_display = ('text', 'file', 'user', 'time', 'text_channel', 'answer_to')
    list_filter = ('user', 'time')


admin.site.register(Channel, ChannelAdmin)
admin.site.register(ChannelText, ChannelTextAdmin)
admin.site.register(ChannelVoice, ChannelVoiceAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageReply, MessageReplyAdmin)
admin.site.register(Privilege, PrivilegeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(ServerUser, ServerUserAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Rights, RightsAdmin)
admin.site.register(RightsRole, RightsRoleAdmin)
admin.site.register(RightsServerUser, RightsServerUserAdmin)