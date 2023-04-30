import pytest
from mixer.backend.django import mixer as _mixer

from book.read.models import Book


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def book_1(user):
    return Book.objects.create(title='Тест 1', author=user, text='hello')


@pytest.fixture
def book_1(user):
    return Book.objects.create(title='Тест 2', author=user, text='hello')