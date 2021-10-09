import uuid, time, random

from . import logger


logger = logger.Logger("room")
exception_logger = logger.gen_exception_logger()


class Room:
  def __init__(self, settings):
    self.settings = settings

    self.state = 0
    self.players = {}
    self.deck = []
    self.order = []


  @exception_logger(fail_output=False)
  def validate(self):
    if self.settings["players_count"] > 52 // 4:
      raise Exception("Room settings doesn't meet the required constraints.")

    return True


  @exception_logger(fail_output=False)
  def update(self):
    if self.state in [0]:
      if len(self.players) == self.settings["players_count"]:
        self.deck = list(range(52))
        self.order = list(self.players.keys())
        random.shuffle(self.order)
        for pid in self.players:
          self.players[pid]["ready"] = 0
          self.players[pid]["cards"] = []
          for _ in range(4):
            card = random.choice(self.deck)
            self.deck.remove(card)
            self.players[pid]["cards"].append(card)
        self.state = 1

    elif self.state in [1]:
      self.order = self.order[1:] + self.order[:1]
      if all([player["ready"] in [1] for player in self.players.values()]):
        for pid in self.players:
          if pid in self.order:
            self.players[pid]["ready"] = 0
          if (len(self.players[pid]["cards"]) == 0 or
              len(self.players[pid]["cards"]) == 52):
            self.players[pid]["ready"] = 2
            self.order.remove(pid)
      if len(self.order) == 0:
        self.state = 2


  @exception_logger(fail_output=("-1", {}))
  def add_player(self, nickname):
    if self.state not in [0]:
      raise Exception("This action is not allowed at the current game state.")

    player = {
      "identification": list(self.players.keys()),
      "nickname": nickname,
      "ready": 0,
      "cards": []
    }

    player_id = str(uuid.uuid4())
    for pid in self.players:
      self.players[pid]["identification"].append(player_id)

    self.players[player_id] = player

    return player_id, self.settings


  @exception_logger(fail_output=([], -1, []))
  def get_state(self, player_id):
    self.__wait_state([0, 1], player_id)

    if self.state not in [0, 1]:
      raise Exception("This action is not allowed at the current game state.")

    if player_id not in self.players:
      raise Exception("Player with given 'player_id' wasn't found.")

    cards = self.players[player_id]["cards"]

    turn = None
    if self.order[0] == player_id:
      turn = -1
    else:
      self.players[player_id]["indentification"].find(player_id)

    players = []
    for pid in self.players:
      if player_id != pid:
        player = {}
        player["nickname"] = self.players[pid]["nickname"]
        player["ready"] = self.players[pid]["ready"]
        player["cards_count"] = len(self.players[pid]["cards"])
        players.append(player)

    state = {
      "cards": cards,
      "turn": turn,
      "players": players
    }

    return state


  @exception_logger(fail_output=-1)
  def take_card(self, player_id, target_index, card):
    self.__wait_state([1], player_id)

    if self.state not in [1]:
      raise Exception("This action is not allowed at the current game state.")

    if player_id not in self.players:
      raise Exception("Player with given 'player_id' wasn't found.")

    if not (0 <= target_index < len(self.players)):
      raise Exception("Parameter 'target_index' out of bounds.")

    if card not in self.players[player_id]["cards"]:
      raise Exception("Player doesn't have specified card.")

    target_pid = self.players[player_id]["indentification"][target_index]

    if self.order[0] != target_pid:
      raise Exception("It's not target player's turn.")

    self.players[player_id]["cards"].remove(card)
    self.players[target_pid]["cards"].append(card)

    return 1


  @exception_logger(fail_output=-1)
  def set_ready(self, player_id):
    self.__wait_state([1], player_id)

    if self.state not in [1]:
      raise Exception("This action is not allowed at the current game state.")

    if player_id not in self.players:
      raise Exception("Player with given 'player_id' wasn't found.")

    if self.players[player_id]["ready"] == 2:
      raise Exception("Player is already finished a game.")

    self.players[player_id]["ready"] = 1
    if self.order[0] == player_id:
      if len(self.deck) > 0:
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.players[player_id]["cards"].append(card)

    return self.players[player_id]["ready"]


  def __wait_state(self, states, player_id=None):
    if player_id and self.players[player_id]["ready"] == 2:
      return False

    self.update()
    while self.state not in states:
      time.sleep(1)

    return True
