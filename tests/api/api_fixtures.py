from src import app
import pytest


@pytest.fixture
def client():
  with app.test_client() as client:
    yield client


@pytest.fixture
def room_data_2(client):
  result = client.post("/api/createRoom", json={
    "room_settings": {
      "name": "Room_2",
      "players_count": 2
    }
  }).json
  return result


@pytest.fixture
def room_data_3(client):
  result = client.post("/api/createRoom", json={
    "room_settings": {
      "name": "Room_3",
      "players_count": 3
    }
  }).json
  return result


@pytest.fixture
def join_data_2(client, room_data_2):
  result = []
  for i in range(2):
    join_data = client.post("/api/joinRoom", json={
      "room_id": room_data_2["room_id"],
      "nickname": f"Player_{i}"
    }).json
    result.append(join_data)
  return result


@pytest.fixture
def join_data_3(client, room_data_3):
  result = []
  for i in range(3):
    join_data = client.post("/api/joinRoom", json={
      "room_id": room_data_3["room_id"],
      "nickname": f"Player_{i}"
    }).json
    result.append(join_data)
  return result
