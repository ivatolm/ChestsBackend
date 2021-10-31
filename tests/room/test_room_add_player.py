from src import tools
from room_fixtures import *


def test_room_add_player_ok(room_data_2):
  assert room_data_2.state in [0]

  player_id, room_settings = room_data_2.add_player(f"Player_{0}")

  assert isinstance(player_id, str) and player_id != "-1"
  assert isinstance(room_settings, dict) and room_settings == room_data_2.settings
