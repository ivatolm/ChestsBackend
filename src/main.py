from flask import Flask

app = Flask(
  __name__,
  static_url_path='',
  static_folder='static',
  template_folder='templates'
)

# Connecting modules to the server
from api import *

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
