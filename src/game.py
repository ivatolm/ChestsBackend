import uuid

from . import logger
from .room import Room


logger = logger.Logger("game")
exception_logger = logger.gen_exception_logger()


class Game:
  def __init__(self):
    self.rooms = {}
    self.players = {}


  @exception_logger(fail_output="-1")
  def create_room(self, room_settings):
    room = Room(room_settings)
    if not room.validate():
      raise Exception("Failed to create room with given parameters.")

    id = str(uuid.uuid4())

    if (
      (type(room_settings["name"]) != str)
        or
      (type(room_settings["players_count"]) != int)
    ):
      raise Exception("'room_settings' doesn't meet the required constraints.")

    if id not in self.rooms:
      self.rooms[id] = room
      return id

    raise Exception("Unique id generation failed.")


  @exception_logger(fail_output=("-1", {}))
  def join_room(self, join_params):
    room_id, nickname = join_params["room_id"], join_params["nickname"]

    if room_id in self.rooms and type(nickname) == str:
      player_id, room_settings = self.rooms[room_id].add_player(nickname)
      self.players[player_id] = room_id
      return player_id, room_settings

    raise Exception("Invalid room id.")


  @exception_logger(fail_output=(-1, [], []))
  def get_state(self, state_params):
    player_id = state_params["player_id"]

    if player_id in self.players:
      room_id = self.players[player_id]
      result = self.rooms[room_id].get_state(player_id)
      return result

    raise Exception("Invalid player id.")


  @exception_logger(fail_output=False)
  def take_card(self, take_params):
    room_id, player_id, nickname, card = (
      take_params["player_id"],
      take_params["nickname"],
      take_params["card"]
    )

    if player_id in self.players:
      room_id = self.players[player_id]
      result = self.rooms[room_id].take_card(player_id, nickname, card)
      return result

    raise Exception("Invalid player id.")


  @exception_logger(fail_output=False)
  def set_ready(self, ready_params):
    player_id = ready_params["player_id"]

    if player_id in self.players:
      room_id = self.players[player_id]
      result = self.rooms[room_id].set_ready(player_id)
      return result

    raise Exception("Invalid player id.")
