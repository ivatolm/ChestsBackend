from src import tools
from src.room import Room


def test_room_take_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 2
  }
  nickname_1 = "Developer_1"
  nickname_2 = "Developer_2"

  room = Room(room_settings)
  player_id_1, _ = room.add_player(nickname_1)
  player_id_2, _ = room.add_player(nickname_2)

  turn_1, cards_1 = room.state(player_id_1)
  turn_2, cards_2 = room.state(player_id_2)

  result = None
  if turn_1:
    result = room.take(player_id_1, nickname_2, cards_2[0])
  elif turn_2:
    result = room.take(player_id_2, nickname_1, cards_1[0])
  assert result == True

  player_1 = room.players[player_id_1]
  assert tools.validate(player_1, {
    "nickname": str,
    "ready": bool,
    "turn": bool,
    "cards": list,
    "state": int
  })
  assert player_1["ready"] == False
  assert player_1["nickname"] == nickname_1
  assert player_1["state"] == 2
  if turn_1:
    assert len(player_1["cards"]) == 5
    assert player_1["cards"] == cards_1 + cards_2[0]
  else:
    assert len(player_1["cards"]) == 3

  player_2 = room.players[player_id_2]
  assert tools.validate(player_2, {
    "nickname": str,
    "ready": bool,
    "turn": bool,
    "cards": list,
    "state": int
  })
  assert player_2["ready"] == False
  assert player_2["nickname"] == nickname_2
  assert player_2["state"] == 2
  if turn_2:
    assert len(player_2["cards"]) == 5
    assert player_2["cards"] == cards_2 + cards_1[0]
  else:
    assert len(player_2["cards"]) == 3

  assert room.st == 1
