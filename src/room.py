import uuid, time, random

from . import logger


lggr = logger.Logger("room")


class Room:
  def __init__(self, settings):
    self.settings = settings

    self.state = 0
    self.players = {}
    self.deck = []
    self.order = []


  def validate(self):
    if self.settings["players_count"] > 52 // 4:
      raise Exception(301)

    return True


  def update(self, dummy=False):
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
      if not dummy:
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


  def add_player(self, nickname):
    if self.state not in [0]:
      raise Exception(302)

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


  def get_state(self, player_id):
    self.__wait_state([0, 1], player_id)

    if self.state not in [0, 1]:
      raise Exception(302)

    if player_id not in self.players:
      raise Exception(303)

    cards = self.players[player_id]["cards"]

    turn = None
    if self.order[0] == player_id:
      turn = -1
    else:
      turn = self.players[player_id]["identification"].index(self.order[0])

    players = []
    for pid in self.players:
      if player_id != pid:
        player = {}
        player["nickname"] = self.players[pid]["nickname"]
        player["ready"] = self.players[pid]["ready"]
        player["cards_count"] = len(self.players[pid]["cards"])
        players.append(player)

    return (cards, turn, players)


  def give_card(self, player_id, target_index, card):
    self.__wait_state([1], player_id)

    if self.state not in [1]:
      raise Exception(302)

    if player_id not in self.players:
      raise Exception(303)

    if not (0 <= target_index < len(self.players) - 1):
      raise Exception(304)

    if card not in self.players[player_id]["cards"]:
      raise Exception(305)

    target_pid = self.players[player_id]["identification"][target_index]

    if self.order[0] != target_pid:
      raise Exception(306)

    self.players[player_id]["cards"].remove(card)
    self.players[target_pid]["cards"].append(card)

    return 1


  def set_ready(self, player_id):
    self.__wait_state([1], player_id)

    if self.state not in [1]:
      raise Exception(302)

    if player_id not in self.players:
      raise Exception(303)

    if self.players[player_id]["ready"] == 2:
      raise Exception(307)

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

    self.update(dummy=True)
    while self.state not in states:
      time.sleep(1)

    return True
