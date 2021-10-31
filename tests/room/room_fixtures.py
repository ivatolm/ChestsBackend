from src import room
import pytest


@pytest.fixture
def room_data_2():
  result = room.Room({
    "name": "Room_2",
    "players_count": 2
  })
  return result


@pytest.fixture
def room_data_3():
  result = room.Room({
    "name": "Room_3",
    "players_count": 3
  })
  return result


@pytest.fixture
def join_data_2(room_data_2):
  result = []
  for i in range(2):
    join_data = room_data_2.add_player(f"Player_{i}")
    result.append(join_data)
  return result


@pytest.fixture
def join_data_3(room_data_3):
  result = []
  for i in range(3):
    join_data = room_data_3.add_player(f"Player_{i}")
    result.append(join_data)
  return result


@pytest.fixture
def deck_52():
  return list(range(52))
