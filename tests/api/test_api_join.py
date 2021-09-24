from src import tools
from api_fixtures import *


def test_api_join_ok(client, room_data_2):
  for i in range(2):
    join_data = client.post("/api/joinRoom", json={
      "room_id": room_data_2["room_id"],
      "nickname": f"Player_{i}"
    }).json

    assert tools.validate(join_data, {
      "player_id": str,
      "room_settings": dict
    })
