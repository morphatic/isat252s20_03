"""A FizzBuzz program"""

# import necessary supporting libraries or packages
from numbers import Number

def fizz(x):
  """
    Takes an input `x` and checks to see if it is a
    number, and if so, also a multiple of 3.
    If it is both, return 'fizz'.
    Otherwise, return the input.
  """
  if isinstance(x, Number) and x % 3 == 0:
    # yes, it is a number and a multiple of 3
    return 'fizz'
  else:
    # no, it is NOT a number or not a mulitple of 3
    return x