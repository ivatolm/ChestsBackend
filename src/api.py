from flask import Flask, request

from . import app, game
from . import logger, tools


lggr = logger.Logger("api")
exception_logger = lggr.gen_exception_logger()


@app.route("/api/createRoom", methods=["POST"], endpoint="create_room")
@exception_logger(fail_output=False)
def create_room():
  data = request.json

  if not tools.validate(data, {
    "room_settings": dict
  }):
    raise Exception(101)
  
  if not tools.validate(data["room_settings"], {
    "name": str,
    "players_count": int
  }):
    raise Exception(101)

  room_id = game.create_room(data)
  return {
    "room_id": room_id
  }


@app.route("/api/joinRoom", methods=["POST"], endpoint="join_room")
@exception_logger(fail_output=False)
def join_room():
  data = request.json

  if not tools.validate(data, {
    "room_id": str,
    "nickname": str
  }):
    raise Exception(101)

  player_id, room_settings = game.join_room(data)
  return {
    "player_id": player_id,
    "room_settings": room_settings
  }


@app.route("/api/getState", methods=["POST"], endpoint="get_state")
@exception_logger(fail_output=False)
def get_state():
  data = request.json

  if not tools.validate(data, {
    "player_id": str
  }):
    raise Exception(101)

  turn, cards, finished = game.get_state(data)
  return {
    "turn": turn,
    "cards": cards,
    "finished": finished
  }


@app.route("/api/giveCard", methods=["POST"], endpoint="give_card")
@exception_logger(fail_output=False)
def give_card():
  data = request.json

  if not tools.validate(data, {
    "player_id": str,
    "nickname": str,
    "card": int
  }):
    raise Exception(101)

  result = game.give_card(data)
  return {
    "status": result
  }


@app.route("/api/setReady", methods=["POST"], endpoint="set_ready")
@exception_logger(fail_output=False)
def set_ready():
  data = request.json

  if not tools.validate(data, {
    "player_id": str
  }):
    raise Exception(101)

  result = game.set_ready(data)
  return {
    "status": result
  }
