from src import game
from game_fixtures import *


def test_game_state_ok(join_data_2):
  for join_data in join_data_2:
    state_data = game.get_state({
      "player_id": join_data[0]
    })

    assert type(state_data) == tuple and len(state_data) == 3
    turn, cards, finished = state_data

    assert (
      type(turn) == bool and
      type(cards) == list and
      type(finished) == list
    )


def test_game_state_non_valid_player_id(join_data_2):
  for _ in join_data_2:
    state_data = game.get_state({
      "player_id": 0
    })

    assert type(state_data) == tuple and len(state_data) == 3
    turn, cards, finished = state_data

    assert (
      type(turn) == int and
      type(cards) == list and
      type(finished) == list
    )

  assert (
    turn == -1 and
    cards == [] and
    finished == []
  )
