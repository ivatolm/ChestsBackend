from src import app

import socket
IP_ADDRESS = socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
  app.run(host=IP_ADDRESS, port=5000, debug=True)
