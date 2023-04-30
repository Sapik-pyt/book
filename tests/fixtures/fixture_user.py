import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from book.read.models import User


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        sername='TestUser',
        password='1234567',
        first_name='t',
        last_name='t2',
        birthday='2020-01-01',
    )

@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        sername='TestUser2',
        password='12345672',
        first_name='t2',
        last_name='t3',
        birthday='2020-01-01',
    )


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient
    token = Token.objects.get(user__username='lauren')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client
