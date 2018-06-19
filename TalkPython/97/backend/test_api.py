import uuid
from flask import json
import pytest

from app import app


@pytest.fixture
def client():
    app.config.from_object('config.TestingConfig')
    client = app.test_client()

    yield client


@pytest.fixture
def user(client):
    user = client.get('api/user/bob')

    yield json.loads(user.data)


@pytest.fixture
def user2(client):
    user = client.get('api/user/testapi')

    yield json.loads(user.data)


def test_get_user(client):
    """
    Test get user endpoint
    :param client:
    """
    resp = client.get('/api/user/bob')
    resp_json = json.loads(resp.data)

    assert resp_json.get('id') == 1
    assert resp_json.get('name') == 'bob'


def test_create_user(client):
    """
    Test create user endpoint
    :param client:
    """

    endpoint = '/api/user'

    # Test value present in name
    resp = client.post(endpoint)
    assert resp.status_code == 400
    assert b'No value for name' in resp.data

    resp = client.post(endpoint, json={
        'name': ' '
    })
    assert resp.status_code == 400
    assert b'No value for name' in resp.data

    # Create with name
    name = uuid.uuid4()
    resp = client.post(endpoint, json={
        'name': name
    })
    resp_json = json.loads(resp.data)
    assert resp_json.get('done')

    # Create with same name
    resp = client.post(endpoint, json={
        'name': name
    })
    assert b'Player already exist' in resp.data


def test_create_game(client):
    """
    Test create game endpoint
    :param client:
    """
    resp = client.post('/api/game')
    resp_json = json.loads(resp.data)

    assert 'id' in resp_json


def test_make_a_guess(client, user, user2):
    endpoint = '/api/guess'

    # Test no body
    resp = client.post(endpoint)
    assert resp.status_code == 400
    assert b'no JSON body' in resp.data

    # Test Id Player
    resp = client.post(endpoint, json={})
    assert resp.status_code == 400
    assert b'no player id'

    resp = client.post(endpoint, json={
        'id_player': 'johny'
    })
    assert resp.status_code == 400
    assert b'incorrect id_player value' in resp.data

    resp = client.post(endpoint, json={
        'id_player': 100000000000000
    })
    assert resp.status_code == 400
    assert b'player not found' in resp.data

    # Test Id Game
    resp = client.post(endpoint, json={
        'id_player': user.get('id')
    })
    assert resp.status_code == 400
    assert b'no game id'

    # Test guess
    resp = client.post(endpoint, json={
        'id_player': user.get('id'),
        'id_game': uuid.uuid4()
    })
    assert resp.status_code == 400
    assert b'no guess provided.' in resp.data

    resp = client.post(endpoint, json={
        'id_player': user.get('id'),
        'id_game': uuid.uuid4(),
        'guess': 'a'
    })
    assert resp.status_code == 400
    assert b'guess is not a valid value.' in resp.data

    resp = client.post(endpoint, json={
        'id_player': user.get('id'),
        'id_game': uuid.uuid4(),
        'guess': 400
    })
    assert resp.status_code == 400
    assert b'guess must be include/equal between 0 and 100' in resp.data

    id_game = uuid.uuid4()
    resp = client.post(endpoint, json={
        'id_player': user.get('id'),
        'id_game': id_game,
        'guess': 40
    })
    resp_json = json.loads(resp.data)
    assert resp.status_code == 200
    assert 'status' in resp_json

    # Test id game
    resp = client.post(endpoint, json={
        'id_player': user2.get('id'),
        'id_game': id_game
    })
    assert resp.status_code == 400
    assert b'this player can\'t play this game.' in resp.data

    # Test game done
    id_game = uuid.uuid4()
    guess = 1

    while True and guess < 101:
        resp = client.post(endpoint, json={
            'id_player': user.get('id'),
            'id_game': id_game,
            'guess': guess
        })

        guess += 1

        if resp.status_code == 400:
            break
    else:
        resp = client.post(endpoint, json={
            'id_player': user.get('id'),
            'id_game': id_game,
            'guess': guess
        })
        assert b'game done.' not in resp.data



