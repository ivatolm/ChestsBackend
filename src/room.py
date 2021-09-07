import uuid, time, random

from . import logger


logger = logger.Logger("room")


class Room:
  def __init__(self, settings):
    self.settings = settings
    self.players = {}
    self.st = 0
    self.deck = [i for i in range(1, 52 + 1)]


  def add_player(self, nickname):
    if self.st != 0:
      return "-1", {}

    player_id = str(uuid.uuid4())

    if player_id in self.players:
      logger.log(__name__, "Unique id generation failed.")
      player_id = "-1"
    else:
      self.players[player_id] = {
        "nickname": nickname,
        "ready": False,
        "turn": False,
        "cards": [],
        "state": 0
      }

      if len(self.players) == self.settings["players_count"]:
        self.st = 1
        for player_id in self.players.keys():
          self.players[player_id]["state"] = 1

    return player_id, self.settings


  def set_ready(self, player_id):
    if self.st != 1:
      return False

    if player_id in self.players:
      if self.players[player_id]["state"] != 2:
        return False

      self.players[player_id]["state"] = 3
      self.players[player_id]["ready"] = True
      return True
    else:
      logger.log(__name__, "Player with given id wasn't found.")
      return False

 
  def wait(self, player_id):
    if self.st != 1:
      return False

    if player_id in self.players:
      if self.players[player_id]["state"] != 3:
        return False

      while (
        (len(self.players) != self.settings["players_count"])
          or
        (False in [player["ready"] for player in self.players.values()])
      ):
        time.sleep(1)
      self.players[player_id]["state"] = 1
      self.players[player_id]["ready"] = False

      return True
    else:
      logger.log(__name__, "Player with given id wasn't found.")
      return False


  def state(self, player_id):
    if self.st != 1:
      return (-1, [])

    if player_id in self.players:
      if self.players[player_id]["state"] != 1:
        return (-1, [])

      self.players[player_id]["state"] = 2
      return (
        self.players[player_id]["turn"],
        list(self.players[player_id]["cards"]),
      )
    else:
      logger.log(__name__, "Player with given id wasn't found.")
      return False


  def take(self, player_id, nickname, card):
    if self.st != 1:
      return False

    if (
      (player_id in self.players)
        and
      (nickname in [player["nickname"] for player in self.players.values()])
    ):
      if self.players[player_id]["state"] != 2:
        return False

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
        logger.log(__name__, "Target player doesn't have specified card.") 
        return False
    else:
      logger.log(__name__, "Player with given id or nickname wasn't found.")
      return False


  def pull(self, player_id):
    if self.st != 1:
      return False

    if player_id in self.players:
      if self.players[player_id]["state"] != 2:
        return False

      card = random.choice(self.deck)
      self.players[player_id]["cards"].append(card)
      self.deck.remove(card)
      return True
    else:
      logger.log(__name__, "Player with given id wasn't found.")
      return False
