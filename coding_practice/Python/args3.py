# Unpacking a List or Tuple into *args

def multiply(*args):
  result = 1  # Initial value
  for i in args:
    result *=i
  return result

numbers = (2,3,5,)
print(multiply(*numbers))   