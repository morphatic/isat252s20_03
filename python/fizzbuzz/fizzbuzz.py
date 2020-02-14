"""A FizzBuzz program"""

# import necessary supporting libraries or packages
from numbers import Number

def fizz(x):
  # determine if x is a number or not
  if isinstance(x, Number):
    # yes, it is a number
    return x % 3 == 0
  else:
    # no, it is NOT a number
    return False