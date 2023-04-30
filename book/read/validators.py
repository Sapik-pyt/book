import datetime
import re

from django.core.exceptions import ValidationError


def validate_username(name):
    """
    Проверка корректоности введенного логина.
    """
    if re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', name) is None:
        raise ValidationError(
            'Логин должен содержать только буквы и цифры',
            params={'name': name}
        )


def validate_first_name_or_last_name(name):
    """
    Проверка корректоности имени пользователя.
    """
    if not name.isalpha():
        raise ValidationError("Имя должно состоять только из букв")


def validate_birthday(data: str):
    """
    Проверка корректности введеной даты рождения.
    """
    min_date_value = "1900-00-00"
    data_now = str(datetime.datetime.now().today().date().strftime("%Y-%m-%d"))
    if not min_date_value <= str(data) <= data_now:
        raise ValidationError('Неверная дата рождения')
