from src import game
from fixtures import *


def test_game_pull_ok(room_data_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.state({
      "room_id": room_data_2["room_id"],
      "player_id": join_data["player_id"]
    })
    states_data.append(state_data)

  for join_data, state_data in zip(join_data_2, states_data):
    if state_data[0]:
      result = game.pull({
        "room_id": room_data_2["room_id"],
        "player_id": join_data["player_id"]
      })

      assert type(result) == bool
      assert result == True


def test_game_pull_non_valid_room_id(room_data_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.state({
      "room_id": room_data_2["room_id"],
      "player_id": join_data["player_id"]
    })
    states_data.append(state_data)

  for join_data, state_data in zip(join_data_2, states_data):
    if state_data[0]:
      result = game.pull({
        "room_id": 0,
        "player_id": join_data["player_id"]
      })

      assert type(result) == bool
      assert result == False


def test_game_pull_non_valid_player_id(room_data_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.state({
      "room_id": room_data_2["room_id"],
      "player_id": join_data["player_id"]
    })
    states_data.append(state_data)

  for _, state_data in zip(join_data_2, states_data):
    if state_data[0]:
      result = game.pull({
        "room_id": room_data_2["room_id"],
        "player_id": 0
      })

      assert type(result) == bool
      assert result == False
