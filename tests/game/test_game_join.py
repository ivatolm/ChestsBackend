from src import game
from game_fixtures import *


def test_game_join_ok(room_data_2):
  for i in range(1):
    player_id, _ = game.join_room({
      "room_id": room_data_2,
      "nickname": f"Player_{i}"
    })

    assert type(player_id) == str
    assert player_id != "-1"


def test_game_join_fill(room_data_2):
  player_ids = set()
  for i in range(2):
    player_id, _ = game.join_room({
      "room_id": room_data_2,
      "nickname": f"Player_{i}"
    })
    player_ids.add(player_id)

    assert type(player_id) == str
    assert player_id != "-1"
  assert len(player_ids) == 2


def test_game_join_overfill(room_data_2):
  for i in range(3):
    player_id, _ = game.join_room({
      "room_id": room_data_2,
      "nickname": f"Player_{i}"
    })

    assert type(player_id) == str
    if i < 2:
      assert player_id != "-1"
    else:
      assert player_id == "-1"


def test_game_join_non_valid_room_id():
  for i in range(2):
    player_id, _ = game.join_room({
      "room_id": 0,
      "nickname": f"Player_{i}"
    })

    assert type(player_id) == str
    assert player_id == "-1"


def test_game_join_non_valid_nickname(room_data_2):
  for _ in range(2):
    player_id, _ = game.join_room({
      "room_id": room_data_2,
      "nickname": 0
    })

    assert type(player_id) == str
    assert player_id == "-1"
