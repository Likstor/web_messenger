from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, View
from app_models.models import Server
from app_models.models import ChannelText
from app_models.models import User
from app_models.models import ServerUser
from django.contrib.auth.mixins import LoginRequiredMixin


class ServerDetailView(LoginRequiredMixin, DetailView):
    model = Server
    template_name = "web_msg/server/server_base.html"
    context_object_name = "server"
    # print(dir(DetailView))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = {'users_list': User.objects.all()}
        # context['channeltext'] = ChannelText.objects.get()
        return context