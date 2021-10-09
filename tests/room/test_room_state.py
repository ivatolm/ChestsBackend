from src import tools
from room_fixtures import *


def test_room_state_ok(room_2, join_data_2):
  for i, join_data in enumerate(join_data_2):
    state_data = room_2.get_state(join_data[0])

    assert type(state_data) == tuple
    assert len(state_data) == 3

    cards, turn, players = state_data
    assert (
      type(cards) == list and
      type(turn) == int and
      type(players) == list
    )

    player = room_2.players[join_data[0]]
    assert tools.validate(player, {
      "identification": list,
      "nickname": str,
      "ready": int,
      "cards": list
    })
    assert player["nickname"] == f"Player_{i}"
