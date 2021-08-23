from flask import Flask, request

from . import app
from . import logger, tools
from . import server


API_LOGGER = logger.Logger()

@app.route("/api/createRoom", methods=["POST"])
def create_room():
  try:
    data = request.json

    if tools.validate(data, { "name": str, "players_count": int }):
      room_id = server.create_room(data["name"], data["players_count"])
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
  try:
    data = request.json()

    if tools.validate(data, { "room_id": str, "nickname": str }):
      server.join_room(data["room_id"], data["nickname"])
    else:
      raise Exception("Data validation failed.")

  except Exception as e:
    API_LOGGER.log("API :: JoinRoom", str(e))


@app.route("/api/ready", methods=["POST"])
def ready():
  try:
    data = request.json()

    if tools.validate(data, { "player_id": str, "ready": bool }):
      server.ready(data["player_id"], data["ready"])
    else:
      raise Exception("Data validation failed.")

  except Exception as e:
    API_LOGGER.log("API :: Ready", str(e))
