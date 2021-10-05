import uuid, time, random

from . import logger


logger = logger.Logger("room")
exception_logger = logger.gen_exception_logger()


class Room:
  def __init__(self, settings):
    self.settings = settings

    self.state = 0
    self.players = {}


  @exception_logger(fail_output=False)
  def validate(self):
    if self.settings["players_count"] > 52 // 4:
      raise Exception("Room settings doesn't meet the required constraints.")

    return True


  @exception_logger(fail_output=False)
  def update(self):
    if self.st == 0:
      pass

    elif self.st == 1:
      pass

    elif self.st == 2:
      pass

    elif self.st == 3:
      pass


  @exception_logger(fail_output=("-1", {}))
  def add_player(self, nickname):
    return "", self.settings


  @exception_logger(fail_output=(-1, [], []))
  def get_state(self, player_id):
    return (), -1, ()


  @exception_logger(fail_output=False)
  def take_card(self, player_id, nickname, card):
    return 0


  @exception_logger(fail_output=False)
  def set_ready(self, player_id):
    return 0
