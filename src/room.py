import uuid, time, random

from . import logger


logger = logger.Logger("room")
exception_logger = logger.gen_exception_logger()


class Room:
  def __init__(self, settings):
    self.settings = settings
    self.players = {}
    self.st = 0
    self.turn = 0
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
        "order": -1,
        "turn": False,
        "wait": False
      }

      self.players[player_id]["wait"] = True

      if self.__can_ch_st():
        order = [i for i in range(len(self.players))]
        random.shuffle(order)

        for ord_pos, p_id in zip(order, self.players.keys()):
          for _ in range(4):
            if len(self.deck) == 0:
              raise Exception("Deck is empty.")

            card = random.choice(self.deck)
            self.deck.remove(card)
            self.players[p_id]["cards"].append(card)

          self.players[p_id]["order"] = ord_pos

          if ord_pos == 0:
            self.players[p_id]["turn"] = True

      self.__try_ch_st(1)

      return player_id, self.settings

    raise Exception("Unique id generation failed.")


  @exception_logger(fail_output=(-1, []))
  def state(self, player_id):
    if not self.__wait_st(1, player_id):
      raise Exception("Failed to block on state-change waiting.")

    if player_id in self.players:
      self.players[player_id]["wait"] = True
      self.__try_ch_st(2)

      return (
        self.players[player_id]["turn"],
        list(self.players[player_id]["cards"]),
        list(self.finished)
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
  def set_ready(self, player_id):
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
          self.players[p_id]["order"] = -1
          self.finished.add(player["nickname"])

    next_order_turn = None
    for p_id, player in self.players.items():
      turn, order = player["turn"], player["order"]
      if turn:
        next_order_turn = (order + 1) % self.settings["players_count"]
        self.players[p_id]["turn"] = False
        break

    if next_order_turn == None:
      raise Exception("Nobody is making a move.")

    for p_id, player in self.players.items():
      order = player["order"]
      if order == next_order_turn:
        self.players[p_id]["turn"] = True
        break

    return True


  @exception_logger(fail_output=False)
  def __wait_st(self, state, player_id):
    if not (
      (self.st == state) or
      (self.players[player_id]["wait"])
    ):
      return False

    while self.st != state:
      time.sleep(1)

    return True


  @exception_logger(fail_output=False)
  def __try_ch_st(self, new_state):
    change_cond = sum([player["wait"] for player in self.players.values()])

    if change_cond == self.settings["players_count"]:
      self.st = new_state
      for player_id, _ in self.players.items():
        self.players[player_id]["wait"] = False
      return True

    return False


  @exception_logger(fail_output=False)
  def __can_ch_st(self):
    change_cond = sum([player["wait"] for player in self.players.values()])

    if change_cond == self.settings["players_count"]:
      return True
    return False
