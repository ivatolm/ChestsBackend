from src import tools
from fixtures import *


def test_api_take_ok(client):
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

  take_data = client.post("/api/take", json={
    "room_id": room_data["room_id"],
    "player_id": join_data["player_id"],
    "nickname": "dev",
    "card": 25
  }).json

  assert tools.validate(take_data, {
    "success": bool
  })
