from src import tools
from fixtures import *


def test_api_join_ok(client):
  room_data = client.post("/api/createRoom", json={
    "name": "room name with spaces",
    "players_count": 1
  }).json

  join_data = client.post("/api/joinRoom", json={
    "room_id": room_data["room_id"],
    "nickname": "dev"
  }).json

  assert tools.validate(join_data, {
    "player_id": str,
    "room_settings": dict
  })
