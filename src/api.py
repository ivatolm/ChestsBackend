from flask import Flask, request

from main import app

import tools
import logger

import server


API_LOGGER = logger.Logger()

@app.route("/api/createRoom", methods=["POST"])
def create_room():
  try:
    data = request.json()

    if tools.validate(data, { "name": str, "players_count": int }):
      server.create_room(data["name"], data["players_count"])

  except Exception as e:
    API_LOGGER.log("API :: CreateRoom", str(e))
