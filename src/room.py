import uuid

from . import logger


ROOM_LOGGER = logger.Logger()

class Room:
  def __init__(self, settings):
    self.settings = settings
    self.players = {}


  def add_player(self, nickname):
    player_id = str(uuid.uuid4())

    if player_id in self.players:
      ROOM_LOGGER.log("ROOM :: add_player", "Unique id generation failed.")
      player_id = "-1"
    else:
      self.players[player_id] = { "nickname": nickname }
    
    return player_id, self.settings
