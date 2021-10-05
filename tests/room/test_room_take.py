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

  turn_1, _, _ = room.get_state(player_id_1)
  turn_2, _, _ = room.get_state(player_id_2)

  room.players[player_id_1]["cards"] = [0, 1, 2, 3]
  room.players[player_id_2]["cards"] = [13, 14, 15, 16]
  exception = room.players[player_id_1]["cards"] + room.players[player_id_2]["cards"]
  room.deck = [i for i in range(52) if i not in exception]

  result = None
  if turn_1:
    result = room.take_card(player_id_1, nickname_2, 13)
  elif turn_2:
    result = room.take_card(player_id_2, nickname_1, 1)
  assert result == True

  player_1 = room.players[player_id_1]
  assert tools.validate(player_1, {
    "nickname": str,
    "turn": bool,
    "cards": list,
    "wait": bool,
    "finish": bool
  })
  assert player_1["nickname"] == nickname_1
  if turn_1:
    assert len(player_1["cards"]) == 5
    assert player_1["cards"] == [0, 1, 2, 3] + [13]
  else:
    assert len(player_1["cards"]) == 3

  player_2 = room.players[player_id_2]
  assert tools.validate(player_2, {
    "nickname": str,
    "turn": bool,
    "cards": list,
    "wait": bool,
    "finish": bool
  })
  assert player_2["nickname"] == nickname_2
  if turn_2:
    assert len(player_2["cards"]) == 5
    assert player_2["cards"] == [13, 14, 15, 16] + [1]
  else:
    assert len(player_2["cards"]) == 3
