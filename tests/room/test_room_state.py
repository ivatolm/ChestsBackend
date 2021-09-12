from src import tools
from src.room import Room


def test_room_state_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }
  nickname = "Developer"

  room = Room(room_settings)
  player_id, _ = room.add_player(nickname)

  result = room.state(player_id)
  assert type(result) == tuple
  assert len(result) == 2

  turn, cards = result
  assert type(turn) == bool and type(cards) == list

  player = room.players[player_id]
  assert tools.validate(player, {
    "nickname": str,
    "turn": bool,
    "cards": list,
    "wait": bool,
  })
  assert player["nickname"] == nickname
  assert len(player["cards"]) == 4
