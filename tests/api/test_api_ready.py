from src import tools
from fixtures import *


def test_api_ready_ok(client):
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

  ready_data = client.post("/api/ready", json={
    "room_id": room_data["room_id"],
    "player_id": join_data["player_id"],
    "ready": True
  }).json

  assert tools.validate(ready_data, {
    "success": bool
  })
