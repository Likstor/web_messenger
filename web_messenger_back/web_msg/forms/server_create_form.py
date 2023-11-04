from django import forms
from app_models.models import Server

class ServerCreateForm(forms.Form):
    class Meta:
        model = Server
        fields = ('title')