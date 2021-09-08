import os, json, datetime
from functools import wraps

class Logger:

  CONFIG_FILE = "config.json"

  def __init__(self, name):
    if self.CONFIG_FILE not in os.listdir("."):
      print(f"Couldn't create Logger: config file not found")
      return

    with open(self.CONFIG_FILE, 'r') as config_file:
      config = json.loads(config_file.read())
      if "logFile" not in config:
        print("Couldn't create Logger: 'logFile' property not found")
        return

      self.log_file = config["logFile"]
      self.name = name

    with open(self.log_file, 'w') as log_file:
      log_file.write('')


  def log(self, who, msg):
    with open(self.log_file, 'a') as log_file:
      log_msg = f"{datetime.datetime.now()} :: {self.name} :: {who} :: {str(msg)}\n"
      log_file.write(log_msg)


  def gen_exception_logger(self):
    def exception_logger(*args, **kwargs):
      def func_wrapper(func):
        @wraps(func)
        def wrapper(*w_args, **w_kwargs):
          self.log(func.__name__, ">>>")
          result = None

          try:
            result = func(*w_args, **w_kwargs)
          except Exception as e:
            self.log(func.__name__, str(e))
            result = kwargs["fail_output"]

          self.log(func.__name__, "<<<")
          return result

        return wrapper
      return func_wrapper
    return exception_logger
