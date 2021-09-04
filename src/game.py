import uuid

from . import logger
from .room import Room


GAME_LOGGER = logger.Logger()

class Game:
  def __init__(self):
    self.rooms = {}


  def create_room(self, room_settings):
    room = Room(room_settings)
    id = str(uuid.uuid4())

    if id in self.rooms:
      GAME_LOGGER.log("GAME :: create_room", "Unique id generation failed.")
      id = "-1"
    else:
      self.rooms[id] = room

    return id


  def join_room(self, join_params):
    try:
      room_id, nickname = join_params["room_id"], join_params["nickname"]

      if room_id not in self.rooms:
        raise Exception("Invalid room id.")
      else:
        player_id, room_settings = self.rooms[room_id].add_player(nickname)

      return player_id, room_settings

    except Exception as e:
      GAME_LOGGER.log("GAME :: join_room", str(e))
      return "-1", {}


  def ready(self, ready_params):
    try:
      room_id, player_id = ready_params["room_id"], ready_params["player_id"]

      if room_id not in self.rooms:
        raise Exception("Invalid room id.")
      else:
        result = self.rooms[room_id].set_ready(player_id)
        return result

    except Exception as e:
      GAME_LOGGER.log("GAME :: ready", str(e))
      return False


  def wait(self, wait_params):
    try:
      room_id, player_id = wait_params["room_id"], wait_params["player_id"]

      if room_id not in self.rooms:
        raise Exception("Invalid room id.")
      else:
        result = self.rooms[room_id].wait(player_id)
        return result
    
    except Exception as e:
      GAME_LOGGER.log("GAME :: wait", str(e))
      return False


  def state(self, state_params):
    try:
      room_id, player_id = state_params["room_id"], state_params["player_id"]

      if room_id not in self.rooms:
        raise Exception("Invalid room id.")
      else:
        result = self.rooms[room_id].state(player_id)
        return result

    except Exception as e:
      GAME_LOGGER.log("GAME :: state", str(e))
      return False


  def take(self, take_params):
    try:
      room_id, player_id, nickname, card = (
        take_params["room_id"],
        take_params["player_id"],
        take_params["nickname"],
        take_params["card"]
      )

      if room_id not in self.rooms:
        raise Exception("Invalid room id.")
      else:
        result = self.rooms[room_id].take(player_id, nickname, card)
        return result
  
    except Exception as e:
      GAME_LOGGER.log("GAME :: take", str(e))
      return False
