import uuid, time, random

from . import logger


logger = logger.Logger("room")
exception_logger = logger.gen_exception_logger()


class Room:
  def __init__(self, settings):
    self.settings = settings
    self.players = {}
    self.st = 0
    self.deck = [i for i in range(1, 52 + 1)]


  @exception_logger(fail_output=("-1", {}))
  def add_player(self, nickname):
    if self.st != 0:
      raise Exception("This action isn't allowed in current game state.")

    player_id = str(uuid.uuid4())

    if (
      (player_id not in self.players)
        and
      (nickname not in [player["nickname"] for player in self.players.values()])
    ):
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

    raise Exception("Unique id generation failed.")


  @exception_logger(fail_output=False)
  def set_ready(self, player_id):
    if self.st != 1:
      raise Exception("This action isn't allowed in current game state.")

    if player_id in self.players:
      if self.players[player_id]["state"] != 2:
        raise Exception("This action isn't allowed in current player state.")

      self.players[player_id]["state"] = 3
      self.players[player_id]["ready"] = True
      return True

    raise Exception("Player with given id wasn't found.")

 
  @exception_logger(fail_output=False)
  def wait(self, player_id):
    if self.st != 1:
      raise Exception("This action isn't allowed in current game state.")

    if player_id in self.players:
      if self.players[player_id]["state"] != 3:
        raise Exception("This action isn't allowed in current player state.")

      while (
        (len(self.players) != self.settings["players_count"])
          or
        (False in [player["ready"] for player in self.players.values()])
      ):
        time.sleep(1)
      self.players[player_id]["state"] = 1
      self.players[player_id]["ready"] = False

      return True

    raise Exception("Player with given id wasn't found.")


  @exception_logger(fail_output=(-1, []))
  def state(self, player_id):
    if self.st != 1:
      raise Exception("This action isn't allowed in current game state.")

    if player_id in self.players:
      if self.players[player_id]["state"] != 1:
        raise Exception("This action isn't allowed in current player state.")

      self.players[player_id]["state"] = 2
      return (
        self.players[player_id]["turn"],
        list(self.players[player_id]["cards"]),
      )

    raise Exception("Player with given id wasn't found.")


  @exception_logger(fail_output=False)
  def take(self, player_id, nickname, card):
    if self.st != 1:
      raise Exception("This action isn't allowed in current game state.")

    if (
      (player_id in self.players)
        and
      (nickname in [player["nickname"] for player in self.players.values()])
    ):
      if self.players[player_id]["state"] != 2:
        raise Exception("This action isn't allowed in current player state.")

      target_player = None
      for player_id, player_data in self.players.items():
        if player_data["nickname"] == nickname:
          target_player = player_id
          break

      if card in self.players[target_player]["cards"]:
        self.players[player_id]["cards"].append(card)
        self.players[target_player]["cards"].remove(card)
        return True

      raise Exception("Target player doesn't have specified card.")

    raise Exception("Player with given id or nickname wasn't found.")


  @exception_logger(fail_output=False)
  def pull(self, player_id):
    if self.st != 1:
      raise Exception("This action isn't allowed in current game state.")

    if player_id in self.players:
      if self.players[player_id]["state"] != 2:
        raise Exception("This action isn't allowed in current player state.")

      card = random.choice(self.deck)
      self.players[player_id]["cards"].append(card)
      self.deck.remove(card)
      return True

    raise Exception("Player with given id wasn't found.")
