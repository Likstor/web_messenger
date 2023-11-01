<<<<<<< HEAD

from django.http import HttpResponse
from app_models.models import *

def servers(request):
    servers_list = Server.objects.all()
    out = "\n".join([q.title for q in servers_list])
    return HttpResponse(out)
=======
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'web_msg/home.html', {'section': 'home'})
>>>>>>> login-page
