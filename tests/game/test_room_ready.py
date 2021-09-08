from src import game


def test_room_ready_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  room_id = game.create_room(room_settings)
  player_id, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev"
  })

  game.state({
    "room_id": room_id,
    "player_id": player_id
  })

  game.pull({
    "room_id": room_id,
    "player_id": player_id
  })

  result = game.ready({
    "room_id": room_id,
    "player_id": player_id
  })

  assert type(result) == bool

  assert result == True
