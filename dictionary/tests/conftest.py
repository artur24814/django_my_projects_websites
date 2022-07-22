import pytest
from django.test import Client
from django.contrib.auth.models import User
from words.models import Words, TextWithWord


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user():
    user = User.objects.create_user(username='User1', email='User1@example.com', password='Password1476')
    return user


@pytest.fixture()
def login_user(user, client):
    login_user = client.post('/login/', data={'username': 'User1', 'password': 'Password1476'})
    return login_user

@pytest.fixture
def word(client, user):
    word = Words.objects.create(word='słowo', definition='word', author=user)
    return word

@pytest.fixture
def text_with_word(client, login_user, word):
    text_with_word = TextWithWord.objects.create(word=word,
                                                 text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                                                 )
    return text_with_word
