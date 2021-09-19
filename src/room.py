import uuid, time, random

from . import logger


logger = logger.Logger("room")
exception_logger = logger.gen_exception_logger()


class Room:
  def __init__(self, settings):
    self.settings = settings
    self.players = {}
    self.st = 0
    self.order = []
    self.finished = set()
    self.deck = [i for i in range(52)]


  @exception_logger(fail_output=False)
  def validate(self):
    if self.settings["players_count"] > 52 / 4:
      raise Exception("Room settings doesn't meet the required constraints.")

    return True


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
        "wait": False,
        "finish": False
      }

      self.players[player_id]["wait"] = True

      if self.__can_ch_st():
        self.order = [p_id for p_id in self.players.keys()]
        random.shuffle(self.order)
        self.players[self.order[0]]["turn"] = True

        for p_id in self.players.keys():
          for _ in range(4):
            if len(self.deck) == 0:
              raise Exception("Deck is empty.")

            card = random.choice(self.deck)
            self.deck.remove(card)
            self.players[p_id]["cards"].append(card)

      self.__try_ch_st(1)

      return player_id, self.settings

    raise Exception("Unique id generation failed.")


  @exception_logger(fail_output=(-1, [], []))
  def state(self, player_id):
    if not self.__wait_st(1, player_id):
      raise Exception("Failed to block on state-change waiting.")

    if player_id in self.players:
      self.players[player_id]["wait"] = True
      self.__try_ch_st(2)

      return (
        self.players[player_id]["turn"],
        list(self.players[player_id]["cards"]),
        [player["nickname"] for player in self.players.values() if player["finish"]]
      )

    raise Exception("Player with given id wasn't found.")


  @exception_logger(fail_output=False)
  def take(self, player_id, nickname, card):
    if not self.__wait_st(2, player_id):
      raise Exception("Failed to block on state-change waiting.")

    if (
      (player_id in self.players)
        and
      (nickname in [player["nickname"] for player in self.players.values()])
    ):
      target_player = None
      for target_id, player_data in self.players.items():
        if player_data["nickname"] == nickname:
          target_player = target_id
          break

      denomination = card % 13
      checks = [13 * i + denomination for i in range(4)]

      if (
        (card in self.players[target_player]["cards"])
          and
        (True in [True for check in checks if check in self.players[player_id]["cards"]])
      ):
        self.players[player_id]["cards"].append(card)
        self.players[target_player]["cards"].remove(card)
        return True

      raise Exception("Target player doesn't have specified card.")

    raise Exception("Player with given id or nickname wasn't found.")


  @exception_logger(fail_output=False)
  def pull(self, player_id):
    if not self.__wait_st(2, player_id):
      raise Exception("Failed to block on state-change waiting.")

    if player_id in self.players:
      if len(self.deck) == 0:
        raise Exception("Deck is empty.")

      card = random.choice(self.deck)
      self.players[player_id]["cards"].append(card)
      self.deck.remove(card)

      return True

    raise Exception("Player with given id wasn't found.")


  @exception_logger(fail_output=False)
  def ready(self, player_id):
    if not self.__wait_st(2, player_id):
      raise Exception("Failed to block on state-change waiting.")

    if player_id in self.players:
      self.players[player_id]["wait"] = True

      if self.__can_ch_st():
        self.__change_turn()

      self.__try_ch_st(1)

      return True

    raise Exception("Player with given id wasn't found.")


  @exception_logger(fail_output=False)
  def __change_turn(self):
    if len(self.deck) == 0:
      for p_id, player in self.players.items():
        can_take = []
        for card in player["cards"]:
          denomination = card % 13
          checks = [13 * i + denomination for i in range(4)]
          can_take.extend(checks)

        for card in can_take:
          if card not in player["cards"]:
            break
        else:
          if p_id in self.order:
            self.order.remove(p_id)
          self.players[p_id]["finish"] = True

    if len(self.order) == 0:
      raise Exception("Game finished.")

    self.players[self.order[0]]["turn"] = False
    self.order = self.order[1:] + self.order[:1]
    self.players[self.order[0]]["turn"] = True

    return True


  @exception_logger(fail_output=False)
  def __wait_st(self, state, player_id):
    if self.st == state:
      return True

    if (
      (not self.players[player_id]["wait"]) or
      (self.players[player_id]["finish"])
    ):
      return False

    while self.st != state:
      time.sleep(1)

    return True


  @exception_logger(fail_output=False)
  def __try_ch_st(self, new_state):
    waiting, finished = 0, 0
    for player in self.players.values():
      waiting += player["wait"]
      finished += player["finish"]

    if waiting == self.settings["players_count"] - finished:
      self.st = new_state
      for player_id, _ in self.players.items():
        self.players[player_id]["wait"] = False
      return True

    return False


  @exception_logger(fail_output=False)
  def __can_ch_st(self):
    waiting, finished = 0, 0
    for player in self.players.values():
      waiting += player["wait"]
      finished += player["finish"]

    return waiting == self.settings["players_count"] - finished
