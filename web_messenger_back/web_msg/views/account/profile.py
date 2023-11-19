from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from app_models.models import User


@login_required
def profile(request):
    return render(request, 'web_msg/account/profile.html', {'section': 'account'})


class ProfileDetailView(DetailView):
    model = User
    template_name = "web_msg/server/channel/channel_text.html"
    context_object_name = ""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        server = context['channeltext'].server
        context['server'] = server
        return context