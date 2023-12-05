from django.urls import path
from .views import ServerUserDetailView, ServerUserListView, RoleDetailView, RoleListView, ServerDetailView, ServerListView, ChannelListView, ChannelDetailView, UserListView, UserDetailView, PrivilegeListView, PrivilegeDetailView, ChannelTextListView, ChannelTextDetailView, ChannelVoiceListView, ChannelVoiceDetailView, RightsRoleDetailView, RightsRoleListView, RightsServerUserDetailView, RightsServerUserListView, RightsDetailView, RightsListView, MessageReplyListView, MessageDetailView, MessageListView, MessageReplyDetailView, StatusDetailView, StatusListView

urlpatterns = [
    path('server-users/', ServerUserListView.as_view()),
    path('server-users/<int:pk>/', ServerUserDetailView.as_view()),
    path('roles/', RoleListView.as_view()),
    path('roles/<int:pk>/', RoleDetailView.as_view()),
    path('servers/', ServerListView.as_view()),
    path('servers/<int:pk>/', ServerDetailView.as_view()),
    path('channels/', ChannelListView.as_view()),
    path('channels/<int:pk>/', ChannelDetailView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('text-channels/', ChannelTextListView.as_view()),
    path('text-channels/<int:pk>/', ChannelTextDetailView.as_view()),
    path('voice-channels/', ChannelVoiceListView.as_view()),
    path('voice-channels/<int:pk>/', ChannelVoiceDetailView.as_view()),
    path('privilegies/', PrivilegeListView.as_view()),
    path('privilegies/<int:pk>/', PrivilegeDetailView.as_view()),
    path('messages/', MessageListView.as_view()),
    path('messages/<int:pk>/', MessageDetailView.as_view()),
    path('reply-messages/', MessageReplyListView.as_view()),
    path('reply-messages/<int:pk>/', MessageReplyDetailView.as_view()),
    path('statuses/', StatusListView.as_view()),
    path('statuses/<int:pk>/', StatusDetailView.as_view()),
    path('rights/', RightsListView.as_view()),
    path('rights/<int:pk>/', RightsDetailView.as_view()),
    path('rights-roles/', RightsRoleListView.as_view()),
    path('rights-roles/<int:pk>/', RightsRoleDetailView.as_view()),
    path('rights-server-users/', RightsServerUserListView.as_view()),
    path('rights-server-users/<int:pk>/', RightsServerUserDetailView.as_view())
]