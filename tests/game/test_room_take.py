from src import game


def test_room_take_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 2
  }

  room_id = game.create_room(room_settings)
  player_id_1, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_1"
  })
  player_id_2, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_2"
  })

  game.state({
    "room_id": room_id,
    "player_id": player_id_1
  })

  game.state({
    "room_id": room_id,
    "player_id": player_id_2
  })

  game.pull({
    "room_id": room_id,
    "player_id": player_id_1
  })

  results = []
  for i in range(1, 52 + 1):
    results.append(
      game.take({
        "room_id": room_id,
        "player_id": player_id_2,
        "nickname": "Dev_1",
        "card": i
      })
    )

  assert True in results
