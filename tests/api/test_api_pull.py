from src import tools
from fixtures import *


def test_api_pull_ok(client, room_data_2, join_data_2):
  states_data = []
  for i in range(2):
    state_data = client.post("/api/state", json={
      "room_id": room_data_2["room_id"],
      "player_id": join_data_2[i]["player_id"]
    }).json
    states_data.append(state_data)

  for i, state_data in enumerate(states_data):
    if state_data["turn"] == True:
      pull_data = client.post("/api/pull", json={
        "room_id": room_data_2["room_id"],
        "player_id": join_data_2[i]["player_id"],
      }).json

      assert tools.validate(pull_data, {
        "success": bool
      })
