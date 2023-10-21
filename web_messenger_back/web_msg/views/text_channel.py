from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, View
from ..forms import LoginForm
# from app_models.models import Channel
from app_models.models import TextChannel


class TextChannelDetailView(DetailView):
    model = TextChannel
    template_name = "web_msg/text_channel.html"
    context_object_name = "textchannel"
    

def channel_chat(request):
    return render(request, 'web_msg/text_channel.html')