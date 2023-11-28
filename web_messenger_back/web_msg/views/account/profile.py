from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from app_models.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileDetailView(LoginRequiredMixin, View):
    template_name = "web_msg/account/profile.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)