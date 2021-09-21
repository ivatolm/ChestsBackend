from src import tools
from fixtures import *


def test_api_ready_ok(client, room_data_2, join_data_2):
  for i in range(2):
    _ = client.post("/api/state", json={
      "room_id": room_data_2["room_id"],
      "player_id": join_data_2[i]["player_id"]
    }).json

  for i in range(2):
    ready_data = client.post("/api/ready", json={
      "room_id": room_data_2["room_id"],
      "player_id": join_data_2[i]["player_id"],
      "ready": True
    }).json

    assert tools.validate(ready_data, {
      "success": bool
    })
