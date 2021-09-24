from src import tools
from room_fixtures import *


def test_room_add_player_ok(room_2, deck_52):
  assert room_2.st == 0
  assert room_2.deck == deck_52

  player_ids = []
  for i in range(1):
    player_id, _room_settings = room_2.add_player(f"Player_{i}")
    player_ids.append(player_id)
    assert type(player_id) == str and type(_room_settings) == dict
    assert _room_settings == room_2.settings
    assert len(room_2.players) == i + 1
    assert player_id in room_2.players

    player = room_2.players[player_id]
    assert tools.validate(player, {
      "nickname": str,
      "turn": bool,
      "cards": list,
      "wait": bool,
    })
    assert player["nickname"] == f"Player_{i}"


def test_room_add_player_fill(room_2, deck_52):
  assert room_2.st == 0
  assert room_2.deck == deck_52

  player_ids = []
  for i in range(2):
    player_id, _room_settings = room_2.add_player(f"Player_{i}")
    player_ids.append(player_id)
    assert type(player_id) == str and type(_room_settings) == dict
    assert _room_settings == room_2.settings
    assert len(room_2.players) == i + 1
    assert player_id in room_2.players

    player = room_2.players[player_id]
    assert tools.validate(player, {
      "nickname": str,
      "turn": bool,
      "cards": list,
      "wait": bool,
    })
    assert player["nickname"] == f"Player_{i}"

  for player_id in player_ids:
    player = room_2.players[player_id]
    assert len(player["cards"]) == 4

    for card in player["cards"]:
      deck_52.remove(card)
  assert room_2.deck == deck_52
