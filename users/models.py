from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="E-mail")
    telegram = models.CharField(max_length=64, unique=True, verbose_name="Telegram", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
