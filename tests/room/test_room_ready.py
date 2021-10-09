from src import tools
from room_fixtures import *


def test_room_ready_ok(room_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = room_2.get_state(join_data[0])
    states_data.append(state_data)

  for i, join_data in enumerate(join_data_2):
    result = room_2.set_ready(join_data[0])
    assert result == True

    player = room_2.players[join_data[0]]
    assert tools.validate(player, {
      "identification": list,
      "nickname": str,
      "ready": int,
      "cards": list
    })
    assert player["nickname"] == f"Player_{i}"
