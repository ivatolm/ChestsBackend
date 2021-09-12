from src import tools
from fixtures import *


def test_api_state_ok(client):
  room_data = client.post("/api/createRoom", json={
    "name": "room name with spaces",
    "players_count": 1
  }).json

  join_data = client.post("/api/joinRoom", json={
    "room_id": room_data["room_id"],
    "nickname": "dev"
  }).json

  state_data = client.post("/api/state", json={
    "room_id": room_data["room_id"],
    "player_id": join_data["player_id"]
  }).json
  
  assert tools.validate(state_data, {
    "turn": bool,
    "cards": list
  })
