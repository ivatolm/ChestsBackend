import os, requests, threading, time
from operator import itemgetter

from src.tools import validate

import socket


IP_ADDRESS = socket.gethostbyname(socket.gethostname())
SERVER_URL = f"http://{IP_ADDRESS}:5000"


def req(url, data, ans_type):
  ans = requests.post(url, json=data).json()
  for item in ans_type:
    if item not in ans:
      return {}
  return ans if validate(ans, ans_type) else {}

def _server_thread():
  os.system("python3 ./run.py")

def main():
  server = threading.Thread(target=_server_thread)
  server.start()

  time.sleep(1)

  room_id = itemgetter("roomId")(req(
    f"{SERVER_URL}/api/createRoom",
    {
      "name": "room name with spaces",
      "players_count": 1,
    },
    { "roomId": str }
  ))

  print(room_id)

if __name__ == "__main__":
  main()
