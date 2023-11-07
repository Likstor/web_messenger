from django.shortcuts import render
from django.views.generic import ListView
from app_models.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin, ListView):
    model = Server
    template_name='web_msg/home.html'
    context_object_name = 'my_servers_list'


    def get_queryset(self):
        return (Server.objects.all())