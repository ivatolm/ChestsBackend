from src import game


def test_room_pull_ok():
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

  result = game.pull({
    "room_id": room_id,
    "player_id": player_id
  })

  assert type(result) == bool

  assert result == True


def test_room_pull_non_valid_room_id():
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

  result = game.pull({
    "room_id": 0,
    "player_id": player_id
  })

  assert type(result) == bool

  assert result == False


def test_room_pull_non_valid_player_id():
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

  result = game.pull({
    "room_id": room_id,
    "player_id": 0
  })

  assert type(result) == bool

  assert result == False


def test_room_pull_non_valid_game_state():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  room_id = game.create_room(room_settings)
  player_id, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev"
  })

  result = game.pull({
    "room_id": room_id,
    "player_id": player_id
  })

  assert type(result) == bool

  assert result == False
