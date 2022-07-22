import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_register_user_(client):
    data = {'username': 'User',
            'password1': 'Password1476',
            'password2': 'Password1476',
            }
    response = client.post('/register/', data)
    count_users = User.objects.all().count()

    assert response.status_code == 302
    assert count_users == 1


@pytest.mark.django_db
def test_login_user(client, user):
    response_get = client.get('/login/')
    response_post = client.post('/login/', data={'username': 'User1', 'password': 'Password1476'})

    assert response_get.status_code == 200
    assert response_post.status_code == 302


@pytest.mark.django_db
def test_logout_user(client, login_user):
    response = client.post('/logout/')

    assert response.status_code == 302
