from . import logger


TOOLS_LOGGER = logger.Logger()

def validate(x, y):
  try:
    if not y:
      raise Exception("Sample object is None.")

    result = True
    for key, item in y.items():
      if key not in x:
        result = False

      if not isinstance(x[key], item):
        result = False

      TOOLS_LOGGER.log(
        "DEBUG :: TOOLS :: Validate",
        f"{key} ({type(x[key]).__name__} <> {item.__name__}) > " +
          "PASSED" if result else "FAILED")

    return result

  except Exception as e:
    TOOLS_LOGGER.log("TOOLS :: Validate", str(e))
    return False
