from src import tools
from .room_fixtures import *


def test_room_give_card_ok(room_data_2):
  room_data_2.add_player(f"Player_{0}")
  room_data_2.add_player(f"Player_{1}")
  room_data_2.update()

  player_id = room_data_2.order[1]
  target_index = 0
  card = room_data_2.players[player_id]["cards"][0]

  assert room_data_2.state in [1]

  result = room_data_2.give_card(player_id, target_index, card)

  assert isinstance(result, int) and result == 1
