from src import game


def test_room_join_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 2
  }

  room_id = game.create_room(room_settings)
  player_id, _room_settings = game.join_room({
    "room_id": room_id,
    "nickname": "Dev"
  })

  assert type(player_id) == str
  assert player_id != "-1"

  assert room_settings == _room_settings


def test_room_join_fill():
  room_settings = {
    "name": "DevRoom",
    "players_count": 2
  }

  room_id = game.create_room(room_settings)
  player_id_1, _room_settings_1 = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_1"
  })

  player_id_2, _room_settings_2 = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_2"
  })

  assert type(player_id_1) == type(player_id_2) == str
  assert player_id_1 != "-1" and player_id_2 != "-1"
  assert player_id_1 != player_id_2

  assert _room_settings_1 == _room_settings_2 == room_settings


def test_room_join_overfill():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  room_id = game.create_room(room_settings)
  player_id_1, _room_settings_1 = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_1"
  })

  player_id_2, _room_settings_2 = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_2"
  })

  assert type(player_id_1) == type(player_id_2) == str
  assert player_id_1 != "-1" and player_id_2 == "-1"

  assert _room_settings_1 == room_settings and _room_settings_2 == {}


def test_room_join_same_nicknames():
  room_settings = {
    "name": "DevRoom",
    "players_count": 2
  }

  room_id = game.create_room(room_settings)
  player_id_1, _room_settings_1 = game.join_room({
    "room_id": room_id,
    "nickname": "Dev"
  })

  player_id_2, _room_settings_2 = game.join_room({
    "room_id": room_id,
    "nickname": "Dev"
  })

  assert type(player_id_1) == type(player_id_2) == str
  assert player_id_1 != "-1" and player_id_2 == "-1"

  assert _room_settings_1 == room_settings and _room_settings_2 == {}


def test_room_join_non_valid_room_id():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  _ = game.create_room(room_settings)
  player_id, _room_settings = game.join_room({
    "room_id": 0,
    "nickname": "Dev"
  })

  assert type(player_id) == str
  assert player_id == "-1"

  assert _room_settings == {}


def test_room_join_non_valid_nickname():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  room_id = game.create_room(room_settings)
  player_id, _room_settings = game.join_room({
    "room_id": room_id,
    "nickname": 0
  })

  assert type(player_id) == str
  assert player_id == "-1"

  assert _room_settings == {}


def test_room_join_non_valid_game_state():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  room_id = game.create_room(room_settings)
  player_id, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_1"
  })

  game.state({
    "room_id": room_id,
    "player_id": player_id
  })

  player_id, _room_settings = game.join_room({
    "room_id": room_id,
    "nickname": "Dev_2"
  })

  assert type(player_id) == str
  assert player_id == "-1"

  assert _room_settings == {}
