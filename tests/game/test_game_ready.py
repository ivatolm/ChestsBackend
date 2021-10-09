from src import game
from game_fixtures import *


def test_game_ready_ok(join_data_2):
  for join_data in join_data_2:
    game.get_state({
      "player_id": join_data[0]
    })

  for join_data in join_data_2:
    ready_data = game.set_ready({
      "player_id": join_data[0]
    })

    assert type(ready_data) == int
    assert ready_data == 1


def test_game_ready_non_valid_player_id(join_data_2):
  for join_data in join_data_2:
    game.get_state({
      "player_id": join_data
    })

  for join_data in join_data_2:
    ready_data = game.set_ready({
      "player_id": 0
    })

    print(ready_data)

    assert type(ready_data) == int
    assert ready_data == -1
