from flask import Flask
from .game import Game

ERROR_CODES = {
  101: "Data validation failed",
  201: "Failed to create room with given parameters",
  202: "'room_settings' doesn't meet the required constraints",
  203: "Unique id generation failed",
  204: "Invalid room id",
  205: "Invalid player id",
  301: "Room settings doesn't meet the required constraints",
  302: "This action is not allowed at the current game state",
  303: "Player with given 'player_id' wasn't found",
  304: "Parameter 'target_index' out of bounds",
  305: "Player doesn't have specified card",
  306: "It's not target player's turn",
  307: "Player is already finished a game"
}

# Creating game instance
game = Game()

# Creating flask application
app = Flask(
  __name__,
  static_url_path='',
  static_folder='static',
  template_folder='templates'
)

# Connecting modules to the server
from .api import *