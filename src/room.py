import uuid, time, random

from . import logger


ROOM_LOGGER = logger.Logger()

class Room:
  def __init__(self, settings):
    self.settings = settings
    self.players = {}
    self.turn = None
    self.deck = [i for i in range(1, 52 + 1)]


  def add_player(self, nickname):
    player_id = str(uuid.uuid4())

    if player_id in self.players:
      ROOM_LOGGER.log("ROOM :: add_player", "Unique id generation failed.")
      player_id = "-1"
    else:
      self.players[player_id] = {
        "nickname": nickname,
        "ready": False,
        "turn": False,
        "cards": []
      }

    return player_id, self.settings


  def set_ready(self, player_id):
    if player_id in self.players:
      self.players[player_id]["ready"] = True
      return True
    else:
      ROOM_LOGGER.log("ROOM :: set_ready", "Player with given id wasn't found.")
      return False


  def wait(self, player_id):
    if player_id in self.players:

      while (
        (len(self.players) != self.settings["players_count"])
          or
        (False in [player["ready"] for player in self.players.values()])
      ):
        time.sleep(1)
      self.players[player_id]["ready"] = False

      return True
    else:
      ROOM_LOGGER.log("ROOM :: wait", "Player with given id wasn't found.")
      return False


  def state(self, player_id):
    if player_id in self.players:
      return (
        self.players[player_id]["turn"],
        list(self.players[player_id]["cards"]),
      )
    else:
      ROOM_LOGGER.log("ROOM :: state", "Player with given id wasn't found.")
      return False


  def take(self, player_id, nickname, card):
    if (
      (player_id in self.players)
        and
      (nickname in [player["nickname"] for player in self.players.values()])
    ):
      target_player = None
      for player_id, player_data in self.players.items():
        if player_data["nickname"] == nickname:
          target_player = player_id
          break

      if card in self.players[target_player]["cards"]:
        self.players[player_id]["cards"].append(card)
        self.players[target_player]["cards"].remove(card)
        return True
      else:
        ROOM_LOGGER.log("ROOM :: take", "Target player doesn't have specified card.") 
        return False
    else:
      ROOM_LOGGER.log("ROOM :: take", "Player with given id or nickname wasn't found.")
      return False


  def pull(self, player_id):
    if player_id in self.players:
      card = random.choice(self.deck)
      self.players[player_id]["cards"].append(card)
      self.deck.remove(card)
      return True
    else:
      ROOM_LOGGER.log("ROOM :: pull", "Player with given id wasn't found.")
      return False
