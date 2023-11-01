from django.http import HttpResponse
from django.shortcuts import render
from ...forms import RegistrationForm

def user_registration(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            create_user = registration_form.save(commit=False)
            create_user.set_password(registration_form.cleaned_data['password_1'])
            create_user.save()
            return render(request, 'web_msg/account/registration/registration_done.html', {'create_user': create_user})
    else:
        registration_form = RegistrationForm()
    return render(request, 'web_msg/account/registration/registration.html', {'registration_form': registration_form})