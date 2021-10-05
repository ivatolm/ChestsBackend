from . import logger


logger = logger.Logger("tools")
exception_logger = logger.gen_exception_logger()


@exception_logger(fail_output=False)
def validate(x, y):
  if not y:
    raise Exception("Sample object is None.")

  results = {}
  for key, item in x.items():
    result = True
    if key not in y or not isinstance(item, y[key]):
      result = False
    results[key] = result
    print(f"{key} ({type(item).__name__}) :: " + ("pass" if result else "fail"))

  for key, item in y.items():
    result = True
    if key not in x:
      result = False
    results[key] = result
    print(f"{key}: ({type(item).__name__}) :: " +
      ("pass" if result else "fail"))

  return bool(sum([item for item in results.values()]))
