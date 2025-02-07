# Using *args to Handle Multiple Arguments

def add_numbers(*args):
  return sum(args)  #args is a tuple of all passed numbers

print(add_numbers(1,2,3,4))
print(add_numbers(60,20))