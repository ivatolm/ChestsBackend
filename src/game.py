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
