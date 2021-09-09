from src import tools
from src.room import Room


def test_room_wait_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }
  nickname = "Developer"

  room = Room(room_settings)
  player_id, _ = room.add_player(nickname)
  room.state(player_id)
  room.set_ready(player_id)

  result = room.wait(player_id)
  assert result == True

  player = room.players[player_id]
  assert tools.validate(player, {
    "nickname": str,
    "ready": bool,
    "turn": bool,
    "cards": list,
    "state": int
  })
  assert player["ready"] == False
  assert player["nickname"] == nickname
  assert len(player["cards"]) == 4
  assert player["state"] == 1

  assert room.st == 1
