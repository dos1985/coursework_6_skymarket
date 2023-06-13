from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import YourPasswordResetView

users_router = SimpleRouter()

# обратите внимание, что здесь в роуте мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path('api/users/reset_password/', YourPasswordResetView.as_view(), name='password_reset'),

]
