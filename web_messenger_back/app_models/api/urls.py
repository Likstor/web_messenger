from django.urls import path
from .views import ServerUserView

urlpatterns = [
    path('server-users/', ServerUserView.as_view()),
]