from django.urls import path
from .views import SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", TokenObtainPairView.as_view(), name="login"),
]