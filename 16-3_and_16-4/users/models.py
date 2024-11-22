from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Пользовательская модель пользователя, расширяющая стандартную модель Django.

    Атрибуты:
        age (IntegerField): Возраст пользователя (может быть пустым).
        bio (TextField): Краткая биография пользователя (опционально).
        avatar (ImageField): Аватар пользователя (опционально).
        birth_date (DateField): Дата рождения пользователя (опционально).
    """
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление пользователя (имя пользователя).
        """
        return self.username
