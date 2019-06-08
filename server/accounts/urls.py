from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserView

urlpatterns = [
    path('register/', CreateUserView.as_view()),
    path('login/', obtain_auth_token)
]