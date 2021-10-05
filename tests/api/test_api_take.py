from src import tools
from api_fixtures import *


def test_api_take_ok(client, room_data_2, join_data_2):
  states_data = []
  for i in range(2):
    state_data = client.post("/api/getState", json={
      "room_id": room_data_2["room_id"],
      "player_id": join_data_2[i]["player_id"]
    }).json
    states_data.append(state_data)

  for i, state_data in enumerate(states_data):
    if state_data["turn"] == True:
      take_data = client.post("/api/takeCard", json={
        "room_id": room_data_2["room_id"],
        "player_id": join_data_2[i]["player_id"],
        "nickname": "Player_1" if i != 0 else "Player_2",
        "card": 0
      }).json

      assert tools.validate(take_data, {
        "success": bool
      })
