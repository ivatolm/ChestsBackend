from . import logger


logger = logger.Logger("tools")


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

      logger.log(
        "validate",
        f"{key} ({type(x[key]).__name__} <> {item.__name__}) :: " +
          ("pass" if result else "fail"))

    return result

  except Exception as e:
    logger.log("validate", str(e))
    return False
