from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone_number = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    email_code = models.CharField(max_length=15, verbose_name='Проверочный код', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
