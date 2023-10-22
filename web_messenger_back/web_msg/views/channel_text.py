from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, View
from app_models.models import ChannelText


class ChannelTextDetailView(DetailView):
    model = ChannelText
    template_name = "web_msg/text_channel.html"
    context_object_name = "channeltext"
    

def channel_chat(request):
    return render(request, 'web_msg/text_channel.html')