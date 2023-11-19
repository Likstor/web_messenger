
from django.shortcuts import render
from django.views.generic import ListView
from app_models.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import ServerCreateForm

class Home(LoginRequiredMixin, ListView):
    model = User
    template_name='web_msg/home.html'
    context_object_name = 'my_servers_list'


    def get_queryset(self):
        user = User.objects.get(pk = self.request.user.pk)
        a = user.serveruser_set.all()
        return a
    
    # def create_server(request):
    #     if request.methid == 'POST':
    #         server_create_form = ServerCreateForm(request.POST)
    #         if server_create_form.is_valid():
    #             owner = request.user
    #             create_server = server_create_form.save()
    #             create_server.owner = owner
    #             create_server.save()
    #             return render(request, 'web_msg/home.html', {'create_server': create_server})
    #         else:
    #             server_create_form = ServerCreateForm()
    #             return render(request, 'web_msg/home.html', {'server_create_form': server_create_form})



