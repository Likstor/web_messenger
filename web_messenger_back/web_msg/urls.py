from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="ICQ:Isekai API",
      default_version='v1',
      description="don't click ⬇",
      terms_of_service="https://takeb1nzyto.space/",
      contact=openapi.Contact(email="nepishisudabolsheponyal@nahuy.da"),
      license=openapi.License(name="EDIK PEDIK License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.index, name='index'),
    
    path('sign-in/', 
         auth_views.LoginView.as_view(
             template_name="web_msg/account/sign_in.html",
             redirect_field_name='home', 
             redirect_authenticated_user=True),
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
    path('password-reset', 
         auth_views.PasswordResetView.as_view(
             template_name='web_msg/account/password_reset/password_reset_form.html',
             email_template_name='web_msg/account/password_reset/password_reset_email.html'
             ), 
         name='password_reset', ),
    
    path('password-reset/done', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='web_msg/account/password_reset/password_reset_done.html'
             ), 
         name='password_reset_done'),
    
    path('password-reset/confirm/<uidb64>/<token>', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='web_msg/account/password_reset/password_reset_confirm.html'
             ), 
         name='password_reset_confirm',),
    
    path('password-reset/complete', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='web_msg/account/password_reset/password_reset_complete.html'
             ), 
         name='password_reset_complete', ),
    
    # account
    
    path('account/profile/',
         views.profile,
         name='profile'),
    
    # server

    path('server/<int:pk>/',views.ServerDetailView.as_view(), name='server-detail'),
    path('server/<int:server_id>/channel/<int:channel_id>/', views.ChannelTextDetailView.as_view(), name='channel-detail'),
    # path('channel/<int:pk>/', views.ChannelTextDetailView.as_view(), name='channel-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]