from src import game


def test_game_take_ok():
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

  result = game.take({
    "room_id": room_id,
    "player_id": player_id_2,
    "nickname": "Dev_1",
    "card": 0
  })

  assert type(result) == bool


def test_game_take_non_valid_room_id():
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

  result = game.take({
    "room_id": room_id,
    "player_id": player_id_2,
    "nickname": "Dev_1",
    "card": 0
  })

  assert type(result) == bool


def test_game_take_non_valid_player_id():
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

  result = game.take({
    "room_id": room_id,
    "player_id": player_id_2,
    "nickname": "Dev_1",
    "card": 0
  })

  assert type(result) == bool


def test_game_take_non_valid_nickname():
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

  result = game.take({
    "room_id": room_id,
    "player_id": player_id_2,
    "nickname": "Dev_1",
    "card": 0
  })

  assert type(result) == bool


def test_game_take_non_valid_card():
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

  result = game.take({
    "room_id": room_id,
    "player_id": player_id_2,
    "nickname": "Dev_1",
    "card": 0
  })

  assert type(result) == bool


def test_game_take_non_valid_game_state():
  room_settings = {
    "name": "DevRoom",
    "players_count": 2
  }

  room_id = game.create_room(room_settings)
  _, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_1"
  })
  player_id_2, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_2"
  })
  
  result = game.take({
    "room_id": room_id,
    "player_id": player_id_2,
    "nickname": "Dev_1",
    "card": 0
  })

  assert type(result) == bool

  assert result == False
