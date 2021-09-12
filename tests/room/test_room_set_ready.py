from src import tools
from src.room import Room


def test_room_set_ready_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }
  nickname = "Developer"

  test_deck = [i for i in range(52)]

  room = Room(room_settings)
  player_id, _ = room.add_player(nickname)
  room.state(player_id)

  result = room.set_ready(player_id)
  assert result == True

  player = room.players[player_id]
  assert tools.validate(player, {
    "nickname": str,
    "turn": bool,
    "cards": list,
    "wait": bool,
  })
  assert player["nickname"] == nickname
  assert len(player["cards"]) == 4

  for card in player["cards"]:
    test_deck.remove(card)
  assert room.deck == test_deck


def test_room_set_ready_fill():
  room_settings = {
    "name": "DevRoom",
    "players_count": 2
  }
  nickname_1 = "Developer_1"
  nickname_2 = "Developer_2"

  test_deck = [i for i in range(52)]

  room = Room(room_settings)
  player_id_1, _ = room.add_player(nickname_1)
  player_id_2, _ = room.add_player(nickname_2)

  room.state(player_id_1)
  room.state(player_id_2)

  result_1 = room.set_ready(player_id_1)
  result_2 = room.set_ready(player_id_2)
  assert result_1 == result_2 == True

  player_1 = room.players[player_id_1]
  assert tools.validate(player_1, {
    "nickname": str,
    "turn": bool,
    "cards": list,
    "wait": bool,
  })
  assert player_1["nickname"] == nickname_1
  assert len(player_1["cards"]) == 4

  player_2 = room.players[player_id_2]
  assert tools.validate(player_2, {
    "nickname": str,
    "turn": bool,
    "cards": list,
    "wait": bool,
  })
  assert player_2["nickname"] == nickname_2
  assert len(player_2["cards"]) == 4

  for card in player_1["cards"] + player_2["cards"]:
    test_deck.remove(card)
  assert room.deck == test_deck
