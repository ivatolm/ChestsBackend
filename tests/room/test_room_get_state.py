from src import tools
from room_fixtures import *


def test_room_get_state_ok(room_data_2, join_data_2):
  assert room_data_2.state in [0, 1]

  cards, turn, players = room_data_2.get_state(join_data_2[0][0])

  assert isinstance(cards, list) and cards != []
  assert isinstance(turn, int) and turn != -2
  assert isinstance(players, list) and players != []   
