from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, View
from app_models.models import Server


class ServerDetailView(DetailView):
    model = Server
    template_name = "web_msg/server_page.html"
    context_object_name = "server"
    

def server_home(request):
    return render(request, 'web_msg/server_page.html')