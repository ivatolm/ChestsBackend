from src import game
from game_fixtures import *


def test_game_take_ok(join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.get_state({
      "player_id": join_data[0]
    })
    states_data.append(state_data)

  for i, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take_card({
        "player_id": join_data[0],
        "nickname": "Player_1" if i == 0 else "Player_0",
        "card": 0
      })

      assert type(result) == bool


def test_game_take_non_valid_player_id(join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.get_state({
      "player_id": join_data[0]
    })
    states_data.append(state_data)

  for i, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take_card({
        "player_id": 0,
        "nickname": "Player_1" if i == 0 else "Player_0",
        "card": 0
      })

      assert type(result) == bool
      assert result == False


def test_game_take_non_valid_nickname(join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.get_state({
      "player_id": join_data[0]
    })
    states_data.append(state_data)

  for _, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take_card({
        "player_id": join_data[0],
        "nickname": 0,
        "card": 0
      })

      assert type(result) == bool
      assert result == False


def test_game_take_non_valid_card(join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.get_state({
      "player_id": join_data[0]
    })
    states_data.append(state_data)

  for i, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take_card({
        "player_id": join_data[0],
        "nickname": "Player_1" if i == 0 else "Player_0",
        "card": 0
      })

      assert type(result) == bool
      assert result == False
