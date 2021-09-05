from flask import Flask, request

from . import app, game
from . import logger, tools


API_LOGGER = logger.Logger()


def exceptionLogger(func):
  def wrapper():
    API_LOGGER.log(f"API :: {func.__name__}", "...")

    try:
      return func()

    except Exception as e:
      API_LOGGER.log(f"API :: {func.__name__}", str(e))
      return False

  return wrapper


@app.route("/api/createRoom", methods=["POST"], endpoint="create_room")
@exceptionLogger
def create_room():
  data = request.json

  if not tools.validate(data, {
    "name": str,
    "players_count": int
  }):
    raise Exception("Data validation failed.")

  room_id = game.create_room(data)
  return {
    "room_id": room_id
  }


@app.route("/api/joinRoom", methods=["POST"], endpoint="join_room")
@exceptionLogger
def join_room():
  data = request.json

  if not tools.validate(data, {
    "room_id": str,
    "nickname": str
  }):
    raise Exception("Data validation failed.")

  player_id, room_settings = game.join_room(data)
  return {
    "player_id": player_id,
    "room_settings": room_settings
  }


@app.route("/api/ready", methods=["POST"], endpoint="ready")
@exceptionLogger
def ready():
  data = request.json

  if not tools.validate(data, {
    "room_id": str,
    "player_id": str,
    "ready": bool
  }):
    raise Exception("Data validation failed.")

  result = game.ready(data)
  return {
    "success": result
  }


@app.route("/api/wait", methods=["POST"], endpoint="wait")
@exceptionLogger
def wait():
  data = request.json

  if not tools.validate(data, {
    "room_id": str,
    "player_id": str
  }):
    raise Exception("Data validation failed.")

  result = game.wait(data)
  return {
    "success": result
  }


@app.route("/api/state", methods=["POST"], endpoint="state")
@exceptionLogger
def state():
  data = request.json

  if not tools.validate(data, {
    "room_id": str,
    "player_id": str
  }):
    raise Exception("Data validation failed.")

  turn, cards = game.state(data)
  return {
    "turn": turn,
    "cards": cards
  }


@app.route("/api/take", methods=["POST"], endpoint="take")
@exceptionLogger
def take():
  data = request.json

  if not tools.validate(data, {
    "room_id": str,
    "player_id": str,
    "nickname": str,
    "card": int
  }):
    raise Exception("Data validation failed.")

  result = game.take(data)
  return {
    "success": result
  }


@app.route("/api/pull", methods=["POST"], endpoint="pull")
@exceptionLogger
def pull():
  data = request.json

  if not tools.validate(data, {
    "room_id": str,
    "player_id": str
  }):
    raise Exception("Data validation failed.")

  result = game.pull(data)
  return {
    "success": result
  }
