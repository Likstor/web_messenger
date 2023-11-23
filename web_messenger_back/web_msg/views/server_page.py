from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import View
from app_models.models import Server
from app_models.models import ChannelText
from app_models.models import User
from app_models.models import ServerUser
from django.contrib.auth.mixins import LoginRequiredMixin


class ServerDetailView(LoginRequiredMixin, View):
    model = Server
    template_name = "web_msg/server/server_base.html"
    context_object_name = "server"
    # print(dir(DetailView))

    def get(self, request, *args, **kwargs):
        server = Server.objects.get(pk=kwargs['server_id'])
        try:
            su = server.serveruser_set.get(user=request.user.id)
        except:
            raise Http404

        return render(request, self.template_name, context={'server' : server, 
                                                            'serveruser': su})