def validate(x, y):
  for key, item in y.items():
    if key not in x:
      return False

    if not isinstance(x[key], item):
      return False

  return True
