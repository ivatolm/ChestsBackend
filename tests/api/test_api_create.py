from src import tools
from api_fixtures import *


def test_api_create_ok(client):
  room_data = client.post("/api/createRoom", json={
    "name": "room name with spaces",
    "players_count": 1
  }).json

  assert tools.validate(room_data, {
    "room_id": str
  })
