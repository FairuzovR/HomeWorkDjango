from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog.models import NULLABLE

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email address', max_length=255)
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='Телефон', help_text= 'Введите номер телефона')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='Страна', help_text= 'Введите страну')
    avatar = models.ImageField(upload_to='users/photo/', verbose_name='Аватар', **NULLABLE, help_text= 'Загрузите аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
# Create your models here.
