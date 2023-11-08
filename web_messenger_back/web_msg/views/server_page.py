from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, View
from app_models.models import Server
from app_models.models import ChannelText
from app_models.models import User
from app_models.models import ServerUser


# class ServerDetailView(DetailView):
#     model = Server
#     template_name = "web_msg/server_page.html"
#     context_object_name = "server"

class ServerDetailView(DetailView):
    model = Server
    template_name = "web_msg/server/server_base.html"
    context_object_name = "data"
    # print(dir(DetailView))

    def get_context_data(self, **kwargs):
        user = User.objects.get(pk = self.request.user.id)
        serveruser = user.serveruser_set.all()

        context = super().get_context_data(**kwargs)
        # context = {'users_list': User.objects.all()}
        context['server'] = context['object']
        context['serveruser'] = serveruser
        context['user'] = user

        # context['channeltext'] = ChannelText.objects.get()
        return context


def server_home(request):
    return render(request, 'web_msg/server_base.html')