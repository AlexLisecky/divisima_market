from django.db import models
from django.contrib.auth.models import AbstractUser


class UserMarket(AbstractUser):
    email = models.EmailField(verbose_name='Почта', unique=True)
    avatar = models.ImageField(verbose_name='Аватар', blank=True)
