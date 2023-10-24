
from django.http import HttpResponse
from app_models.models import *

def servers(request):
    servers_list = Server.objects.all()
    out = "\n".join([q.title for q in servers_list])
    return HttpResponse(out)