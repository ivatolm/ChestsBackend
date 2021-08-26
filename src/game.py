import uuid

from . import logger
from .room import Room


GAME_LOGGER = logger.Logger()

class Game:
  def __init__(self):
    self.rooms = {}


  def create_room(self, room_settings):
    room = Room(room_settings)
    id = uuid.uuid4()

    if id in self.rooms:
      GAME_LOGGER.log("GAME :: create_room", "Unique id generation failed.")
      id = "-1"
    else:
      self.rooms[id] = room

    return id
