import uuid

from . import logger
from .room import Room


logger = logger.Logger("game")
exception_logger = logger.gen_exception_logger()


class Game:
  def __init__(self):
    self.rooms = {}


  @exception_logger(fail_output="-1")
  def create_room(self, room_settings):
    room = Room(room_settings)
    id = str(uuid.uuid4())

    if (
      (type(room_settings["name"]) != str)
        or
      (type(room_settings["players_count"]) != int)
        or
      (len(room_settings["name"]) > 50)
        or
      (room_settings["players_count"] > 20)
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
      return player_id, room_settings

    raise Exception("Invalid room id.")


  @exception_logger(fail_output=False)
  def ready(self, ready_params):
    room_id, player_id = ready_params["room_id"], ready_params["player_id"]

    if room_id in self.rooms:
      result = self.rooms[room_id].set_ready(player_id)
      return result

    raise Exception("Invalid room id.")


  @exception_logger(fail_output=False)
  def wait(self, wait_params):
    room_id, player_id = wait_params["room_id"], wait_params["player_id"]

    if room_id in self.rooms:
      result = self.rooms[room_id].wait(player_id)
      return result

    raise Exception("Invalid room id.")


  @exception_logger(fail_output=(-1, []))
  def state(self, state_params):
    room_id, player_id = state_params["room_id"], state_params["player_id"]

    if room_id in self.rooms:
      result = self.rooms[room_id].state(player_id)
      return result

    raise Exception("Invalid room id.")


  @exception_logger(fail_output=False)
  def take(self, take_params):
    room_id, player_id, nickname, card = (
      take_params["room_id"],
      take_params["player_id"],
      take_params["nickname"],
      take_params["card"]
    )

    if room_id in self.rooms:
      result = self.rooms[room_id].take(player_id, nickname, card)
      return result

    raise Exception("Invalid room id.")


  @exception_logger(fail_output=False)
  def pull(self, pull_params):
    room_id, player_id = pull_params["room_id"], pull_params["player_id"]

    if room_id in self.rooms:
      result = self.rooms[room_id].pull(player_id)
      return result

    raise Exception("Invalid room id.")
