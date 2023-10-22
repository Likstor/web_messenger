from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('server/<int:pk>/', views.ServerDetailView.as_view(), name='server-detail'),
    path('channel/<int:pk>/', views.ChannelTextDetailView.as_view(), name='channel-detail')
]