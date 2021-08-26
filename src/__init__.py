from flask import Flask
from .game import Game

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