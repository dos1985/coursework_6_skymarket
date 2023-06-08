from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import UserRoles, UserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField(max_length=20)
    email = models.EmailField(unique=True, max_length=255)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.USER, max_length=10)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя
    objects = UserManager

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
