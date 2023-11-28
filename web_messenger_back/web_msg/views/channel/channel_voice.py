from django.views.generic import DetailView
from app_models.models.channel.channel_voice import ChannelVoice


class ChannelVoiceDetailView(DetailView):
    model = ChannelVoice
    template_name = "web_msg/server/channel/channel_voice.html"
    context_object_name = "channelvoice"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channel_id'] = context['object'].pk
        return context