from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),
    
    path('sign-in/', 
         auth_views.LoginView.as_view(
             template_name="web_msg/account/sign_in.html",
             redirect_field_name='home', redirect_authenticated_user=True),
         name='sign_in'),
    
    path('sign-up/', 
         views.sign_up, 
         name='sign_up'),
    
    path('logout/', 
         auth_views.LogoutView.as_view(
             template_name="web_msg/account/logout.html"), 
         name='logout'),
    
    path('home/', 
         login_required(views.Home.as_view()), 
         name='home'),
    
    # password change
    
    # password reset
    path('account/password-reset', 
         auth_views.PasswordResetView.as_view(
             template_name='web_msg/account/password_reset/password_reset_form.html',
             email_template_name='web_msg/account/password_reset/password_reset_email.html'
             ), 
         name='password_reset', ),
    
    path('account/password-reset/done', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='web_msg/account/password_reset/password_reset_done.html'
             ), 
         name='password_reset_done'),
    
    path('account/password-reset/confirm/<uidb64>/<token>', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='web_msg/account/password_reset/password_reset_confirm.html'
             ), 
         name='password_reset_confirm',),
    
    path('account/password-reset/complete', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='web_msg/account/password_reset/password_reset_complete.html'
             ), 
         name='password_reset_complete', ),

    path('server/<int:pk>/',views.ServerDetailView.as_view(), name='server-detail'),
    # path('server/<int:pk>/channel/<int:pk>/', views.ChannelTextDetailView.as_view(), name='channel-detail'),
    path('channel/<int:pk>/', views.ChannelTextDetailView.as_view(), name='channel-detail')
]