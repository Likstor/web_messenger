from django.views.generic import DetailView
from app_models.models.channel.channel_text import ChannelText


class ChannelTextDetailView(DetailView):
    model = ChannelText
    template_name = "web_msg/server/channel/channel_text.html"
    context_object_name = "channeltext"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channel_id'] = context['object'].pk
        return context