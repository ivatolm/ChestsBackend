from src import tools
from .api_fixtures import *


def test_api_errormap_ok(client):
    codes_data = client.post("/api/getErrorMap", json={
    }).json

    assert tools.validate(codes_data, {
      "error_code": int,
      "map": dict
    })
