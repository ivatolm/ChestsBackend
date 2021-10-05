from src import tools
from api_fixtures import *


def test_api_state_ok(client, join_data_2):
  for i in range(2):
    state_data = client.post("/api/getState", json={
      "player_id": join_data_2[i]["player_id"]
    }).json

    assert tools.validate(state_data, {
      "turn": bool,
      "cards": list,
      "finished": list
    })
