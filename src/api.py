from flask import Flask, request

from . import app, game, ERROR_CODES
from . import logger, tools

lggr = logger.Logger("api")


@app.route("/api/createRoom", methods=["POST"], endpoint="create_room")
def create_room():
  response = {
    "error_code": 0
  }

  try:
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

    room_id = game.create_room(data["room_settings"])
    response = dict(response, **{
      "room_id": room_id
    })
  
  except Exception as e:
    response["error_code"] = int(str(e))
    lggr.log("create_room", str(e))

  return response


@app.route("/api/joinRoom", methods=["POST"], endpoint="join_room")
def join_room():
  response = {
    "error_code": 0
  }

  try:
    data = request.json

    if not tools.validate(data, {
      "room_id": str,
      "nickname": str
    }):
      raise Exception(101)

    player_id, room_settings = game.join_room(data)
    response = dict(response, **{
      "player_id": player_id,
      "room_settings": room_settings
    })

  except Exception as e:
    response["error_code"] = int(str(e))
    lggr.log("join_room", str(e))

  return response


@app.route("/api/getState", methods=["POST"], endpoint="get_state")
def get_state():
  response = {
    "error_code": 0
  }

  try:
    data = request.json

    if not tools.validate(data, {
      "player_id": str
    }):
      raise Exception(101)

    turn, cards, finished = game.get_state(data)
    response = dict(response, **{
      "turn": turn,
      "cards": cards,
      "finished": finished
    })
  
  except Exception as e:
    response["error_code"] = int(str(e))
    lggr.log("get_state", str(e))
  
  return response


@app.route("/api/giveCard", methods=["POST"], endpoint="give_card")
def give_card():
  response = {
    "error_code": 0
  }

  try:
    data = request.json

    if not tools.validate(data, {
      "player_id": str,
      "nickname": str,
      "card": int
    }):
      raise Exception(101)

    result = game.give_card(data)
    response = dict(response, **{
      "status": result
    })

  except Exception as e:
    response["error_code"] = int(str(e))
    lggr.log("give_card", str(e))

  return response


@app.route("/api/setReady", methods=["POST"], endpoint="set_ready")
def set_ready():
  response = {
    "error_code": 0
  }

  try:
    data = request.json

    if not tools.validate(data, {
      "player_id": str
    }):
      raise Exception(101)

    result = game.set_ready(data)
    response = dict(response, **{
      "status": result
    })

  except Exception as e:
    response["error_code"] = int(str(e))
    lggr.log("set_ready", str(e))
  
  return response


@app.route("/api/getErrorMap", methods=["POST"], endpoint="get_error_map")
def get_error_map():
  response = {
    "error_code": 0
  }

  try:
    data = request.json

    if not tools.validate(data, {
    }):
      raise Exception(101)

    response = dict(response, **{
      "map": ERROR_CODES
    })

  except Exception as e:
    response["error_code"] = int(str(e))
    lggr.log("get_error_map", str(e))
  
  return response
