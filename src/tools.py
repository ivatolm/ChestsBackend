from . import logger


lggr = logger.Logger("tools")
exception_logger = lggr.gen_exception_logger()


@exception_logger(fail_output=False)
def validate(x, y):
  results = {}
  for key, item in x.items():
    result = True
    if key not in y or not isinstance(item, y[key]):
      result = False
    results[key] = result
    lggr.log("validate", f"{key} ({type(item).__name__}) :: " +
      ("pass" if result else "fail"))

  for key, item in y.items():
    result = True
    if key not in x:
      result = False
    results[key] = result
    lggr.log("validate", f"{key}: ({type(item).__name__}) :: " +
      ("pass" if result else "fail"))

  final = 1
  for item in results.values():
    final *= item
  return final
