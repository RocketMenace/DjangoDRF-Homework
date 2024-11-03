from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    phone = models.CharField(max_length=20, verbose_name="номер телефона", unique=True)
    city = models.CharField(max_length=100, verbose_name="город")
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
