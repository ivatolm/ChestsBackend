from src import tools
from room_fixtures import *


def test_room_pull_ok(room_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = room_2.state(join_data[0])
    states_data.append(state_data)

  for i, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = room_2.pull(join_data[0])
      assert result == True

    player = room_2.players[join_data[0]]
    assert tools.validate(player, {
      "nickname": str,
      "turn": bool,
      "cards": list,
      "wait": bool,
    })
    assert player["nickname"] == f"Player_{i}"
    if state_data[0]:
      assert len(player["cards"]) == 5
    else:
      assert len(player["cards"]) == 4
