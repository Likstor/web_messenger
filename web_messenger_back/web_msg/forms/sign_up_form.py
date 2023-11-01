from django import forms
from app_models.models import User


class SignUpForm(forms.ModelForm):
    password_1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email', 'user_name')
    
    def check_password(self):
        cd = self.cleaned_data
        if cd['password_1'] != cd['password_2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password_2']