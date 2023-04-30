from django.contrib.auth.models import AbstractUser
from django.db import models
from read.validators import (validate_birthday,
                             validate_first_name_or_last_name,
                             validate_username)


class User(AbstractUser):
    """
    Модель пользователя.
    """
    username = models.CharField(
        max_length=100,
        unique=True,
        validators=(validate_username,),
        verbose_name="Логин",
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        "Имя",
        max_length=100,
        validators=(validate_first_name_or_last_name,),
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=100,
        validators=(validate_first_name_or_last_name,),
        blank=False,
        null=False,
    )

    birthday = models.DateField(
        "День Рождения",
        validators=(validate_birthday,),
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользовтели"

    def __str__(self):
        return f"Имя - {self.first_name}, Фамилия - {self.last_name}"


class Book(models.Model):
    """
    Модель книг.
    """
    title = models.CharField(
        "Название книги",
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор книги",
        related_name="read_book",
    )
    text = models.TextField(
        "Описание книги",
        max_length=1000,
        blank=False,
        null=False,
    )
    pub_date = models.DateTimeField(
        "Дата создания", auto_now_add=True,
    )

    class Meta:
        ordering = ("title",)
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title
