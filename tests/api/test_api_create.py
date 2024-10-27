from src import tools
from .api_fixtures import *


def test_api_create_ok(client):
  room_data = client.post("/api/createRoom", json={
    "room_settings": {
      "name": "room name with spaces",
      "players_count": 1
    }
  }).json

  assert tools.validate(room_data, {
    "error_code": int,
    "room_id": str
  })
