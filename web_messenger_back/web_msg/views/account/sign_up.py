from django.http import HttpResponse
from django.shortcuts import render
from ...forms import SignUpForm

def user_sign_up(request):
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            create_user = sign_up_form.save(commit=False)
            create_user.set_password(sign_up_form.cleaned_data['password_1'])
            create_user.save()
            return render(request, 'web_msg/account/sign_up/sign_up_done.html', {'create_user': create_user})
    else:
        sign_up_form = SignUpForm()
    return render(request, 'web_msg/account/sign_up/sign_up.html', {'sign_up_form': sign_up_form})