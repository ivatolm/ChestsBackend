import pytest
import src.tools as tools

from src import app, room


@pytest.fixture
def client():
  with app.test_client() as client:
    yield client


def test_createRoom(client):
  room_data = client.post("/api/createRoom", json={
    "name": "room name with spaces",
    "players_count": 1
  }).json  
  print(f"Received response: {room_data}")

  assert tools.validate(room_data, {
    "room_id": str
  })


def test_joinRoom(client):
  room_data = client.post("/api/createRoom", json={
    "name": "room name with spaces",
    "players_count": 1
  }).json
  print(room_data["room_id"])

  join_data = client.post("/api/joinRoom", json={
    "room_id": room_data["room_id"],
    "nickname": "dev"
  }).json
  print(f"Received response: {join_data}")

  assert tools.validate(join_data, {
    "player_id": str,
    "room_settings": dict
  })


def test_ready(client):
  room_data = client.post("/api/createRoom", json={
    "name": "room name with spaces",
    "players_count": 1
  }).json
  print(room_data["room_id"])

  join_data = client.post("/api/joinRoom", json={
    "room_id": room_data["room_id"],
    "nickname": "dev"
  }).json
  print(f"Received response: {join_data}")

  ready_data = client.post("/api/ready", json={
    "room_id": room_data["room_id"],
    "player_id": join_data["player_id"],
    "ready": True
  }).json
  print(f"Received response: {ready_data}")

  assert tools.validate(ready_data, {
    "success": bool
  })

  assert ready_data["success"] == True
