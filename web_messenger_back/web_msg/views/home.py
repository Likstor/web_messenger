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



