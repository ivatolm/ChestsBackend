from src import tools
from .room_fixtures import *


def test_room_set_ready_ok(room_data_2):
  player_id_1, _ = room_data_2.add_player(f"Player_{0}")
  _, _ = room_data_2.add_player(f"Player_{1}")
  room_data_2.update()

  assert room_data_2.state in [1]

  result = room_data_2.set_ready(player_id_1)

  assert isinstance(result, int) and result == 1
