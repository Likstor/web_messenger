from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, View
from app_models.models.channel.channel_text import ChannelText


class ChannelTextDetailView(DetailView):
    model = ChannelText
    template_name = "web_msg/server/channel/channel_text.html"
    context_object_name = "channeltext"
    

def channel_chat(request):  
    return render(request, 'web_msg/server/channel/channel_text.html')