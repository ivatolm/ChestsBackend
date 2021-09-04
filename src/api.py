from flask import Flask, request

from . import app, game
from . import logger, tools


API_LOGGER = logger.Logger()

@app.route("/api/createRoom", methods=["POST"])
def create_room():
  API_LOGGER.log("API :: create_room", "...")

  try:
    data = request.json

    if tools.validate(data, { "name": str, "players_count": int }):
      room_id = game.create_room(data)
      return {
        "room_id": room_id
      }

    else:
      raise Exception("Data validation failed.")

  except Exception as e:
    API_LOGGER.log("API :: CreateRoom", str(e))
    return { "success": False }


@app.route("/api/joinRoom", methods=["POST"])
def join_room():
  API_LOGGER.log("API :: join_room", "...")

  try:
    data = request.json

    if tools.validate(data, { "room_id": str, "nickname": str }):
      player_id, room_settings = game.join_room(data)
      return {
        "player_id": player_id,
        "room_settings": room_settings
      }

    else:
      raise Exception("Data validation failed.")

  except Exception as e:
    API_LOGGER.log("API :: JoinRoom", str(e))
    return { "success": False }


@app.route("/api/ready", methods=["POST"])
def ready():
  API_LOGGER.log("API :: Ready", "...")

  try:
    data = request.json

    if tools.validate(data, { "room_id": str, "player_id": str, "ready": bool }):
      result = game.ready(data)
      return { "success": result }
    
    else:
      raise Exception("Data validation failed.")

  except Exception as e:
    API_LOGGER.log("API :: Ready", str(e))
    return { "success": False }


@app.route("/api/wait", methods=["POST"])
def wait():
  API_LOGGER.log("API :: Wait", "...")

  try:
    data = request.json

    if tools.validate(data, { "room_id": str, "player_id": str }):
      result = game.wait(data)
      return { "success": result }

    else:
      raise Exception("Data validation failed.")

  except Exception as e:
    API_LOGGER.log("API :: Wait", str(e))
    return { "success": False }


@app.route("/api/state", methods=["POST"])
def state():
  API_LOGGER.log("API :: State", "...")

  try:
    data = request.json

    if tools.validate(data, { "room_id": str, "player_id": str }):
      turn, cards = game.state(data)
      return {
        "turn": turn,
        "cards": cards
      }

    else:
      raise Exception("Data validation failed.")

  except Exception as e:
    API_LOGGER.log("API :: State", str(e))
    return { "success": False }
