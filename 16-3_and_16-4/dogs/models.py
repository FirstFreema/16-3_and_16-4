from django.db import models


class Breed(models.Model):
    """
    Модель породы собак.

    Атрибуты:
        name (CharField): Название породы.
        description (TextField): Описание породы.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """
        Возвращает название породы.
        """
        return self.name


class Dog(models.Model):
    """
    Модель собаки.

    Атрибуты:
        name (CharField): Имя собаки.
        breed (ForeignKey): Связь с породой (Breed).
        age (IntegerField): Возраст собаки.
        image (ImageField): Изображение собаки (опционально).
    """
    name = models.CharField(max_length=255)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs')
    age = models.IntegerField()
    image = models.ImageField(upload_to='dogs/', null=True, blank=True)

    def __str__(self):
        """
        Возвращает строковое представление собаки (имя собаки).
        """
        return self.name


class Pet(models.Model):
    """
    Модель домашнего питомца.

    Атрибуты:
        name (CharField): Имя питомца.
        age (IntegerField): Возраст питомца.
        breed (CharField): Порода питомца.
        description (TextField): Описание питомца (опционально).
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление питомца (имя питомца).
        """
        return self.name
