from . import logger


TOOLS_LOGGER = logger.Logger()

def validate(x, y):
  try:
    if not y:
      raise Exception("Sample object is None.")

    for key, item in y.items():
      TOOLS_LOGGER.log("DEBUG :: TOOLS :: Validate", f"{x}, {key}, {item}")

      if key not in x:
        return False

      if not isinstance(x[key], item):
        return False


    return True

  except Exception as e:
    TOOLS_LOGGER.log("TOOLS :: Validate", str(e))
    return False
