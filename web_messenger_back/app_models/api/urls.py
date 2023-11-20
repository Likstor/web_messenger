from django.urls import path
from .views import ServerUserView, RoleView, ServerView, ChannelView, UserView, PrivilegeView, ChannelTextView, ChannelVoiceView, RightsRoleView, RightsServerUserView, RightsView, MessageReplyView, MessageView, StatusView

urlpatterns = [
    path('server-users/', ServerUserView.as_view()),
    path('roles/', RoleView.as_view()),
    path('servers/', ServerView.as_view()),
    path('channels/', ChannelView.as_view()),
    path('users/', UserView.as_view()),
    path('text-channels/', ChannelTextView.as_view()),
    path('voice-channels/', ChannelVoiceView.as_view()),
    path('privilegies/', PrivilegeView.as_view()),
    path('messages/', MessageView.as_view()),
    path('reply-messages/', MessageReplyView.as_view()),
    path('statuses/', StatusView.as_view()),
    path('rights/', RightsView.as_view()),
    path('rights-roles/', RightsRoleView.as_view()),
    path('rights-server-users/', RightsServerUserView.as_view())
]