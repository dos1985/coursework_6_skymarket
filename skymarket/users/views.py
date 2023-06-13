from django.contrib.auth.views import PasswordResetView
from django.views.generic import ListView
from djoser.serializers import UserSerializer
from .models import User


class UserListAPIView(ListView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class YourPasswordResetView(PasswordResetView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

