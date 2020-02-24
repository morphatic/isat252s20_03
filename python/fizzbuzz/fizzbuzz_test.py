# pylint: disable=unused-variable
"""Unit tests for FizzBuzz."""

# import the code to be tested
from fizzbuzz import fizz, buzz, fibu

#import the method needed to test for exceptions
from pytest import raises

def describe_a_fizzbuzz_program_that():
  """A program to play the FizzBuzz game."""

  def has_a_smoke_test():
    """Make sure our testing infrastructure is working."""
    assert True == True

  def describes_a_fizz_function_that():
    """Tests for the fizz() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as err_info:
        fizz() # pylint: disable=no-value-for-parameter
      assert err_info.type == TypeError
      assert 'missing 1 required positional argument' in str(err_info.value)

    def returns_fizz_if_a_number_is_a_multiple_of_3():
      """
        Takes an input `x` and checks to see if it is a
        number, and if so, also a multiple of 3.
        If it is both, return 'fizz'.
        Otherwise, return the input.
      """
      assert fizz(3) == 'fizz'      # multiple of 3
      assert fizz(2) == 2           # non-multiple of 3
      assert fizz(3.5) == 3.5       # non-integer
      assert fizz(0) == 'fizz'      # zero
      assert fizz(-3) == 'fizz'     # negative multiple of 3
      assert fizz(-4) == -4         # negative non-multiple of 3
      assert fizz('buzz') == 'buzz' # non-numeric input

  def describes_a_buzz_function_that():
    """Tests for the buzz() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as err_info:
        buzz() # pylint: disable=no-value-for-parameter
      assert err_info.type == TypeError
      assert 'missing 1 required positional argument' in str(err_info.value)

    def returns_buzz_if_a_number_is_a_multiple_of_5():
      """
        Takes an input `x` and checks to see if it is a
        number, and if so, also a multiple of 5.
        If it is both, return 'buzz'.
        Otherwise, return the input.
      """
      assert buzz(5) == 'buzz'      # multiple of 5
      assert buzz(2) == 2           # non-multiple of 5
      assert buzz(5.5) == 5.5       # non-integer
      assert buzz(0) == 'buzz'      # zero
      assert buzz(-5) == 'buzz'     # negative multiple of 5
      assert buzz(-4) == -4         # negative non-multiple of 5
      assert buzz('fizz') == 'fizz' # non-numeric input

  def describes_a_fibu_function_that():
    """Tests for the fibu() function"""

    def throws_an_error_if_no_input():
      with raises(Exception) as err_info:
        fibu() # pylint: disable=no-value-for-parameter
      assert err_info.type == TypeError
      assert 'missing 1 required positional argument' in str(err_info.value)

    def returns_fizzbuzz_if_a_number_is_a_multiple_of_15():
      """
        Takes an input `x` and checks to see if it is a
        number, and if so, also a multiple of 15.
        If it is both, return 'fizzbuzz'.
        Otherwise, return the input.
      """
      assert fibu(15) == 'fizzbuzz'  # multiple of 15
      assert fibu(2) == 2            # non-multiple of 15
      assert fibu(5.5) == 5.5        # non-integer
      assert fibu(0) == 'fizzbuzz'   # zero
      assert fibu(-15) == 'fizzbuzz' # negative multiple of 15
      assert fibu(-4) == -4          # negative non-multiple of 15
      assert fibu('fizz') == 'fizz'  # non-numeric input
