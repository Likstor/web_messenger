from django.views.generic import DetailView
from app_models.models.channel.channel_text import ChannelText
from app_models.models.user.user import User

class ChannelTextDetailView(DetailView):
    model = ChannelText
    template_name = "web_msg/server/channel/channel_text.html"
    context_object_name = "channeltext"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.pk)
        
        context['channel_id'] = context['object'].pk
        # context['userlocalname'] = user.serveruser_set.get(server_id= context['object'].server_id)
        # print(f"AAAA {context['userlocalname']}")
        return context