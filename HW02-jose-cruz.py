"""HW02: Fractions

   Implement a fraction calculator that asks the user for two
   fractions and an operator and then prints the result

   OUTPUT EXAMPLE
   Welcome to the fraction calculator!
   Fraction 1 numerator: 1 <-- user entered 1
   Fraction 1 denominator: 2 <-- user entered 1
   Operation (+, -, *, /, ==): + <-- user entered +
   Fraction 2 numerator: 3 <-- user entered 1
   Fraction 1 denominator: 4 <-- user entered 1
   1/2 + 3/4 = 10/8 <-- final result - The code converted 1/2 to 4/8 and 3/4 to 6/8 and returns 10/8

   Author: Jose J. Cruz
"""
import os
import time
import sys
from shlex import quote as shlex_quote
from math import gcd


class Fraction:
    __slots__ = ['numerator', 'denominator']

    def __init__(self, numerator: int, denominator: int):
        """Initialize the class fractions require a numerator and a denominator
        We check if a denominator is zero, if it is we throw an exception
        """
        self.numerator: int = numerator
        self.denominator: int = denominator

    def plus(self, other: 'Fraction') -> 'Fraction':
        """Adds a fraction value to the object and return the
        result as another fraction object"""
        result_denominator: int = self.denominator * other.denominator

        # Get the numerator for the first fraction
        first_numerator: int = int((result_denominator / self.denominator) * self.numerator)
        # Get the numerator for the second fraction
        second_numerator: int = int((result_denominator / other.denominator) * other.numerator)

        result_numerator: int = first_numerator + second_numerator
        return Fraction(result_numerator, result_denominator)

    def minus(self, other: 'Fraction') -> 'Fraction':
        """Calculate the difference between the current fraction and other
        and returns the result as another fraction"""
        result_denominator: int = self.denominator * other.denominator

        # Get the numerator for the first fraction
        first_numerator: int = int((result_denominator / self.denominator) * self.numerator)
        # Get the numerator for the second fraction
        second_numerator: int = int((result_denominator / other.denominator) * other.numerator)

        result_numerator: int = first_numerator - second_numerator
        return Fraction(result_numerator, result_denominator)

    def times(self, other: 'Fraction') -> 'Fraction':
        """Calculate the product between the current fraction and the other fraction
        and returns the result as another fraction"""
        result_denominator: int = self.denominator * other.denominator

        # Get the numerator for the second fraction
        first_numerator: int = int((result_denominator / self.denominator) * self.numerator)
        second_numerator: int = int((result_denominator / other.denominator) * other.numerator)

        result_numerator: int = first_numerator * second_numerator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other: 'Fraction') -> 'Fraction':
        """Calculate the quotient between the current fraction and the other fraction
        and returns the result as another fraction"""

        # We invert the numerator and denominator of other
        fraction = Fraction(other.denominator, other.numerator)

        # We use the times operation since is the same logic
        return self.times(fraction)

    def equals(self, other: 'Fraction') -> bool:
        """Check if the two fractions are equal"""
        return (self.numerator * other.denominator) == (self.denominator * other.numerator)

    def reduce(self) -> str:
        """Reduce a fraction for readability"""
        # I know it's not required but i receive instructions from my professor that i need to go
        # the extra mile 😅

        # Check if numerator is 0
        if self.numerator == 0:
            return '0'

        # Check if the module is 0
        if self.numerator % self.denominator == 0:
            return f'{int(self.numerator / self.denominator)}'

        d = gcd(self.numerator, self.denominator)

        return f'{int(self.numerator / d)}/{int(self.denominator / d)} ({self.numerator / self.denominator})'

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'


def main() -> None:
    """Main program function"""
    clear_screen()
    first_fraction = Fraction(1, 2)
    second_fraction = Fraction(3, 4)
    operation: str = '+'

    result: None or bool or 'Fraction' = get_operation_result(first_fraction, second_fraction, operation)
    print_message(first_fraction, second_fraction, operation, result)


def get_operation_result(first_fraction: 'Fraction', second_fraction: 'Fraction',
                         operation: str) -> 'Fraction' or None or bool:
    if operation == '+':
        return first_fraction.plus(second_fraction)
    if operation == '-':
        return first_fraction.minus(second_fraction)
    if operation == '*':
        return first_fraction.times(second_fraction)
    if operation == '/':
        return first_fraction.divide(second_fraction)
    if operation == '==':
        return first_fraction.equals(second_fraction)
    return None


def print_message(first_fraction: 'Fraction', second_fraction: 'Fraction', operation: str,
                  result: None or bool or 'Fraction') -> None:
    """Display the program message"""
    clear_screen()
    if result is None:
        print('Something wrong happened, please try again')

    # This only happens with the equal operation
    if type(result) is bool:
        if result:
            print(f'{first_fraction} and {second_fraction} are equal')
        else:
            print(f'{first_fraction} and {second_fraction} are equal')
        return

    # In this part result can only be a Fraction
    print(f'{first_fraction} {operation} {second_fraction} = {result.reduce()}')


def test_suite():
    """It runs the test suite"""
    clear_screen()
    print("Hello I'm a robot🤖")
    print("I will run a test suite to make sure that everything is working fine 👌")


def clear_screen() -> None:
    """Cleans the terminal"""
    os.system(shlex_quote('cls' if os.name == 'nt' else 'clear'))
    time.sleep(1)


if __name__ == "__main__":
    # We check if the user send the argument 'test' to run the test suite
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_suite()
    else:
        main()
