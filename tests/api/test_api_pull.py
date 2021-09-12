from src import tools
from fixtures import *


def test_api_pull_ok(client):
  room_data = client.post("/api/createRoom", json={
    "name": "room name with spaces",
    "players_count": 1
  }).json

  join_data = client.post("/api/joinRoom", json={
    "room_id": room_data["room_id"],
    "nickname": "dev"
  }).json

  client.post("/api/state", json={
    "room_id": room_data["room_id"],
    "player_id": join_data["player_id"]
  }).json

  pull_data = client.post("/api/pull", json={
    "room_id": room_data["room_id"],
    "player_id": join_data["player_id"],
  }).json

  assert tools.validate(pull_data, {
    "success": bool
  })
