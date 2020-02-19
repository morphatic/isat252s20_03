# pylint: disable=unused-variable
"""Unit tests for FizzBuzz."""

# import the code to be tested
from fizzbuzz import fizz

#import the method needed to test for exceptions
from pytest import raises

def describe_a_fizzbuzz_program_that():
  """A program to play the FizzBuzz game."""

  def has_a_smoke_test():
    """Make sure our testing infrastructure is working."""
    assert True == True

  def describes_a_fizz_function_that():
    """Tests for the fizz() function"""

    def throws_an_error_if_input_is_not_a_postive_integer_or_text():
      with raises(TypeError) as err_info:
        fizz() # pylint: disable=no-value-for-parameter

    def can_determine_if_a_number_is_a_multiple_of_3():
      """Checks to see if a given number is a multiple of 3."""
      assert fizz(3) == True       # multiple of 3
      assert fizz(2) == False      # non-multiple of 3
      assert fizz(3.5) == False    # non-integer
      assert fizz(0) == True       # zero
      assert fizz(-3) == True      # negative multiple of 3
      assert fizz(-4) == False     # negative non-multiple of 3
      assert fizz('buzz') == False # non-numeric input
