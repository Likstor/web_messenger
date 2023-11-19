from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, View
from app_models.models.channel.channel_text import ChannelText


class ChannelTextDetailView(DetailView):
    model = ChannelText
    template_name = "web_msg/server/channel/channel_text.html"
    context_object_name = "channeltext"
   
    
class TestChannelTextDetailView(DetailView):
    model = ChannelText
    template_name = "web_msg/server/test_channels.html"
    context_object_name = "channeltext"


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("")
    context = {}
    return render(request, "web_msg/chatPage.html", context)


# def test_channel(request):
#     return render(request, 'web_msg/server/test_channels.html')