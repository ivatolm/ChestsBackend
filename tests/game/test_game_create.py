from src import game
from game_fixtures import *


def test_game_create_ok():
  room_settings = {
    "name": "DevRoom",
    "players_count": 2
  }

  room_id = game.create_room(room_settings)

  assert type(room_id) == str
  assert room_id != "-1"


def test_game_create_non_valid_name():
  room_settings = {
    "name": 0,
    "players_count": 2
  }

  room_id = game.create_room(room_settings)

  assert type(room_id) == str
  assert room_id == "-1"


def test_game_create_non_valid_size():
  room_settings = {
    "name": "DevRoom",
    "players_count": 21
  }

  room_id = game.create_room(room_settings)

  assert type(room_id) == str
  assert room_id == "-1"
