import pytest
from words.models import Words, LikeText, TextWithWord, CommentsText
import json

@pytest.mark.django_db
def test_home_view(client):
    response = client.get('/')
    response_ajax = client.get('/', data={'word': 'some word'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    #not login user, must return status 200, and not create object
    json_data = json.dumps({'text': 'nowy---new'})
    response_post = client.post('/', json_data,
                                content_type='application/json',
                                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
    count_words = Words.objects.all().count()

    assert response.status_code == 200
    assert response_ajax.status_code == 200
    assert response_post.status_code == 200
    assert count_words == 0

@pytest.mark.django_db
def test_dictionary(client):
    response = client.get('/dictionary/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_blog_view(client, text_with_word):
    response = client.get('/blog/')

    assert response.status_code == 200
    assert len(response.context['posts']) == 1
    assert len(response.context['comments']) == 0

@pytest.mark.django_db
def test_create_like(client, login_user, text_with_word):
    response = client.get('/like-post/1/')

    count_likes = LikeText.objects.all().count()
    count_likes_post = TextWithWord.objects.get(id=1)
    assert response.status_code == 302
    assert count_likes == 1
    assert count_likes_post.no_of_likes == 1


@pytest.mark.django_db
def test_create_comment(client, text_with_word, login_user):
    response = client.post('/comment/1/', data={'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit'})

    count_comment = CommentsText.objects.all().count()
    assert response.status_code == 302
    assert count_comment == 1

@pytest.mark.django_db
def test_card_game(client):
    response = client.get('/card-game/')

    assert response.status_code == 200
    #we have 0 word in dictionary, view must return message, and do not create game for as
    assert 'context' not in response.context

@pytest.mark.django_db
def test_frasses_view(client, user, word):
    #not login user
    response_not_login_user = client.get('/frasses/')
    #user log in
    client.post('/login/', data={'username': 'User1', 'password': 'Password1476'})
    response_login_user = client.get('/frasses/')
    response_ajax_get = client.get('/frasses/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

    assert response_not_login_user.status_code == 302
    assert response_login_user.status_code == 200
    assert response_ajax_get.status_code == 200

