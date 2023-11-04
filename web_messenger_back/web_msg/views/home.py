<<<<<<< HEAD
from typing import Any
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from app_models.models import *


class Home(ListView):
    model = Server
    template_name='web_msg/home.html'
    context_object_name = 'my_servers_list'

    def get_queryset(self):
        return Server.objects.all()



=======

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
>>>>>>> ed101c25e887c8c682a6a22dbe681121e0b9767b
