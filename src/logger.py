import os, json, datetime


class Logger:

  CONFIG_FILE = "config.json"

  def __init__(self):
    if self.CONFIG_FILE not in os.listdir("."):
      print(f"Couldn't create Logger: config file not found")
      return

    with open(self.CONFIG_FILE, 'r') as config_file:
      config = json.loads(config_file.read())
      if "logFile" not in config:
        print("Couldn't create Logger: 'logFile' property not found")
        return

      self.log_file = config["logFile"]
    
    with open(self.log_file, 'w') as log_file:
      log_file.write('')


  def log(self, who, msg):
    with open(self.log_file, 'a') as log_file:
      log_msg = f"{datetime.datetime.now()} :: {who} :: {str(msg)}\n"
      log_file.write(log_msg)
