from src import game
from fixtures import *


def test_game_take_ok(room_data_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.state({
      "room_id": room_data_2["room_id"],
      "player_id": join_data["player_id"]
    })
    states_data.append(state_data)

  for i, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take({
        "room_id": room_data_2["room_id"],
        "player_id": join_data["player_id"],
        "nickname": "Player_1" if i == 0 else "Player_0",
        "card": 0
      })

      assert type(result) == bool


def test_game_take_non_valid_room_id(room_data_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.state({
      "room_id": room_data_2["room_id"],
      "player_id": join_data["player_id"]
    })
    states_data.append(state_data)

  for i, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take({
        "room_id": 0,
        "player_id": join_data["player_id"],
        "nickname": "Player_1" if i == 0 else "Player_0",
        "card": 0
      })

      assert type(result) == bool
      assert result == False


def test_game_take_non_valid_player_id(room_data_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.state({
      "room_id": room_data_2["room_id"],
      "player_id": join_data["player_id"]
    })
    states_data.append(state_data)

  for i, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take({
        "room_id": room_data_2["room_id"],
        "player_id": 0,
        "nickname": "Player_1" if i == 0 else "Player_0",
        "card": 0
      })

      assert type(result) == bool
      assert result == False


def test_game_take_non_valid_nickname(room_data_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.state({
      "room_id": room_data_2["room_id"],
      "player_id": join_data["player_id"]
    })
    states_data.append(state_data)

  for _, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take({
        "room_id": room_data_2["room_id"],
        "player_id": join_data["player_id"],
        "nickname": 0,
        "card": 0
      })

      assert type(result) == bool
      assert result == False


def test_game_take_non_valid_card(room_data_2, join_data_2):
  states_data = []
  for join_data in join_data_2:
    state_data = game.state({
      "room_id": room_data_2["room_id"],
      "player_id": join_data["player_id"]
    })
    states_data.append(state_data)

  for i, (join_data, state_data) in enumerate(zip(join_data_2, states_data)):
    if state_data[0]:
      result = game.take({
        "room_id": room_data_2["room_id"],
        "player_id": join_data["player_id"],
        "nickname": "Player_1" if i == 0 else "Player_0",
        "card": 0
      })

      assert type(result) == bool
      assert result == False
