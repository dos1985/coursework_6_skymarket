from django.conf import settings
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=150, null=False, validators=[MinLengthValidator(10)])
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=500, null=True, blank=True)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    text = models.TextField(blank=True, null=False)
    author = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

