from src import game


def test_room_state_ok():
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

  assert len(state) == 2
  turn, cards = state

  assert type(turn) == bool
  assert type(cards) == list
