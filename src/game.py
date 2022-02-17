import uuid

from . import logger
from .room import Room


lggr = logger.Logger("game")


class Game:
  def __init__(self):
    self.rooms = {}
    self.players = {}


  def create_room(self, room_settings):
    if (
      (type(room_settings["name"]) != str)
        or
      (type(room_settings["players_count"]) != int)
    ):
      raise Exception(202)

    room = Room(room_settings)
    if not room.validate():
      raise Exception(201)

    id = str(uuid.uuid4())

    if id not in self.rooms:
      self.rooms[id] = room
      return id

    raise Exception(203)


  def join_room(self, join_params):
    room_id, nickname = join_params["room_id"], join_params["nickname"]

    if room_id in self.rooms and type(nickname) == str:
      player_id, room_settings = self.rooms[room_id].add_player(nickname)
      self.players[player_id] = room_id

      self.rooms[room_id].update()

      return player_id, room_settings

    raise Exception(204)


  def get_state(self, state_params):
    player_id = state_params["player_id"]

    if player_id in self.players:
      room_id = self.players[player_id]
      result = self.rooms[room_id].get_state(player_id)

      self.rooms[room_id].update()

      return result

    raise Exception(205)


  def give_card(self, give_params):
    room_id, player_id, nickname, card = (
      give_params["player_id"],
      give_params["nickname"],
      give_params["card"]
    )

    if player_id in self.players:
      room_id = self.players[player_id]
      result = self.rooms[room_id].give_card(player_id, nickname, card)

      self.rooms[room_id].update()

      return result

    raise Exception(205)


  def set_ready(self, ready_params):
    player_id = ready_params["player_id"]

    if player_id in self.players:
      room_id = self.players[player_id]
      result = self.rooms[room_id].set_ready(player_id)

      self.rooms[room_id].update()

      return result

    raise Exception(205)
