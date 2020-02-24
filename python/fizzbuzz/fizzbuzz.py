"""A FizzBuzz program"""

# import necessary supporting libraries or packages
from numbers import Number

def fizz(x):
  """
    Takes an input `x` and checks to see if x is a
    number, and if so, also a multiple of 3.
    If it is both, return 'fizz'.
    Otherwise, return the input.
  """
  return 'fizz' if isinstance(x, Number) and x % 3 == 0 else x

def buzz(x):
  """
    Takes an input `x` and checks to see if x is a
    number, and if so, also a multiple of 5.
    If it is both, return 'buzz'.
    Otherwise, return the input.
  """
  return 'buzz' if isinstance(x, Number) and x % 5 == 0 else x

def fibu(x):
  """
    Takes an input `x` and checks to see if x is a
    number, and if so, also a multiple of 15.
    If it is both, return 'fizzbuzz'.
    Otherwise, return the input.
  """
  return 'fizzbuzz' if isinstance(x, Number) and x % 15 == 0 else x
