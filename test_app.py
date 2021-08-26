import pytest
import src.tools as tools

from src import app


@pytest.fixture
def client():
  with app.test_client() as client:
    yield client

def test_createRoom(client):
  res = client.post("/api/createRoom", json={
    "name": "room name with spaces",
    "players_count": 1
  }).json  
  print(f"Received response: {res}")

  assert tools.validate(res, { "roomId": str })
