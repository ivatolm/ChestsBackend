from src import game
from game_fixtures import *


def test_game_ready_ok(room_data_2, join_data_2):
  for join_data in join_data_2:
    game.get_state({
      "room_id": room_data_2,
      "player_id": join_data[0]
    })

  for join_data in join_data_2:
    ready_data = game.set_ready({
      "room_id": room_data_2,
      "player_id": join_data[0]
    })

    assert type(ready_data) == bool
    assert ready_data == True


def test_game_ready_non_valid_room_id(room_data_2, join_data_2):
  for join_data in join_data_2:
    game.get_state({
      "room_id": room_data_2,
      "player_id": join_data[0]
    })

  for join_data in join_data_2:
    ready_data = game.set_ready({
      "room_id": 0,
      "player_id": join_data[0]
    })

    assert type(ready_data) == bool
    assert ready_data == False


def test_game_ready_non_valid_player_id(room_data_2, join_data_2):
  for join_data in join_data_2:
    game.get_state({
      "room_id": room_data_2[0],
      "player_id": join_data
    })

  for join_data in join_data_2:
    ready_data = game.set_ready({
      "room_id": room_data_2,
      "player_id": 0
    })

    assert type(ready_data) == bool
    assert ready_data == False
