from django import forms
from app_models.models import User


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'user_name', 'description', 'avatar')