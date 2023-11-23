from typing import Any
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import View
from app_models.models.channel.channel_text import ChannelText
from django.contrib.auth.mixins import LoginRequiredMixin


class ChannelTextDetailView(LoginRequiredMixin, View):
    template_name = "web_msg/server/channel/channel_text.html"
    
    def get(self, request, *args, **kwargs):
        channel = ChannelText.objects.get(id=kwargs['channel_id'])
        
        if kwargs['server_id'] != channel.server.id:
            raise Http404

        return render(request, self.template_name, context={'server' : channel.server, 
                                                            'channeltext': channel})