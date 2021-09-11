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
        "cards": [],
        "turn": False,
        "wait": False
      }

      self.players[player_id]["wait"] = True
      self.__try_ch_st(1)

      return player_id, self.settings

    raise Exception("Unique id generation failed.")


  @exception_logger(fail_output=(-1, []))
  def state(self, player_id):
    if not self.__wait_st(1):
      raise Exception("Failed to block on state-change waiting.")

    if player_id in self.players:
      self.players[player_id]["wait"] = True
      self.__try_ch_st(2)

      return (
        self.players[player_id]["turn"],
        list(self.players[player_id]["cards"]),
      )

    raise Exception("Player with given id wasn't found.")


  @exception_logger(fail_output=False)
  def take(self, player_id, nickname, card):
    if not self.__wait_st(2):
      raise Exception("Failed to block on state-change waiting.")

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

      raise Exception("Target player doesn't have specified card.")

    raise Exception("Player with given id or nickname wasn't found.")


  @exception_logger(fail_output=False)
  def pull(self, player_id):
    if not self.__wait_st(2):
      raise Exception("Failed to block on state-change waiting.")

    if player_id in self.players:
      card = random.choice(self.deck)
      self.players[player_id]["cards"].append(card)
      self.deck.remove(card)
      return True

    raise Exception("Player with given id wasn't found.")


  @exception_logger(fail_output=False)
  def set_ready(self, player_id):
    if not self.__wait_st(2):
      raise Exception("Failed to block on state-change waiting.")

    if player_id in self.players:
      self.players[player_id]["wait"] = True
      self.__try_ch_st(1)

      return True

    raise Exception("Player with given id wasn't found.")


  @exception_logger(fail_output=False)
  def __wait_st(self, state):
    if not (
      (self.st == 0 and state == 1) or
      (self.st == 1 and state == 2) or
      (self.st == 2 and state == 1)
    ):
      return False

    while self.st != state:
      time.sleep(1)

    return True


  @exception_logger(fail_output=False)
  def __try_ch_st(self, new_state):
    change_cond = sum([player["wait"] for player in self.players])

    if change_cond == self.settings["players_count"]:
      self.st = new_state
      for player_id, _ in self.players.items():
        self.players[player_id]["wait"] = False
      return True

    return False
