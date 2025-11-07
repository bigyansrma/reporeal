from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', obtain_auth_token, name='login'),
]