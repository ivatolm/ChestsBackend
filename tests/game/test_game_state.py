from src import game


def test_game_state_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  room_id = game.create_room(room_settings)
  player_id, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev"
  })

  state = game.state({
    "room_id": room_id,
    "player_id": player_id
  })

  assert type(state) == tuple
  assert len(state) == 3
  turn, cards, finished = state

  assert type(turn) == bool
  assert type(cards) == list
  assert type(finished) == list


def test_game_state_non_valid_room_id():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  room_id = game.create_room(room_settings)
  player_id, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev"
  })

  state = game.state({
    "room_id": 0,
    "player_id": player_id
  })

  assert type(state) == tuple
  assert len(state) == 3
  turn, cards, finished = state

  assert type(turn) == int
  assert type(cards) == list
  assert type(finished) == list

  assert turn == -1
  assert cards == []
  assert finished == []


def test_game_state_non_valid_player_id():
  room_settings = {
    "name": "DevRoom",
    "players_count": 1
  }

  room_id = game.create_room(room_settings)
  _, _ = game.join_room({
    "room_id": room_id,
    "nickname": "Dev"
  })

  state = game.state({
    "room_id": room_id,
    "player_id": 0
  })

  assert type(state) == tuple
  assert len(state) == 3
  turn, cards, finished = state

  assert type(turn) == int
  assert type(cards) == list
  assert type(finished) == list

  assert turn == -1
  assert cards == []
  assert finished == []


def test_game_state_non_valid_game_state():
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

  state = game.state({
    "room_id": room_id,
    "player_id": player_id
  })

  assert type(state) == tuple
  assert len(state) == 3
  turn, cards, finished = state

  assert type(turn) == int
  assert type(cards) == list
  assert type(finished) == list

  assert turn == -1
  assert cards == []
  assert finished == []
