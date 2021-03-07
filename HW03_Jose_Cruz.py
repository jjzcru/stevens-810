"""HW03: Fractions Unit Tests

   Test the Fraction object using the unittest package

   Assignment:
   1. Overwrite the methods to use pythons magic methods:
        __add__()
        __sub__()
        __mul__()
        __truediv__()
        __eq__()
   2. Add new methods:
        __ne__(self, other: "Fraction"): not equal
        __lt__(self, other: "Fraction"): less than
        __le__(self, other: "Fraction"): less than or equal to
        __gt__(self, other: "Fraction"): greater than
        __ge__(self, other: "Fraction"): greater than or equal to
   3. Use Python’s unittest to replace the test cases from your
   Homework 02 submission with unittest self.assert*() tests
   4. Along with the new methods and test suite, you will also get
   some experience using the Python debugger.

   CONVENTIONS:
   - Max character limit per line 80
   - CapWords for class names
   - snake_case for variables and functions

   Author: Jose J. Cruz
"""
import os
import time
import sys
from shlex import quote as shlex_quote
from math import gcd


def gcf(numerator: int, denominator: int) -> int:
    """Calculate the Greatest Common Denominator using Euclid's Algorithm

        Reference:
        http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
     """
    numerator = abs(numerator)
    denominator = abs(denominator)
    if denominator == 0:
        return numerator
    else:
        return gcf(denominator, numerator % denominator)


class Fraction:
    __slots__ = ['numerator', 'denominator']

    def __init__(self, numerator: int, denominator: int):
        """Initialize the class fractions require a numerator and a denominator
        We check if a denominator is zero, if it is we throw an exception
        """
        if denominator == 0:
            raise ValueError('invalid fraction denominator can not be zero')
        self.numerator: int = numerator
        self.denominator: int = denominator

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Adds a fraction value to the object and return the
        result as another fraction object"""
        result_denominator: int = self.denominator * other.denominator

        # Get the numerator for the first fraction
        first_numerator: int = int(
            (result_denominator / self.denominator) * self.numerator)
        # Get the numerator for the second fraction
        second_numerator: int = int(
            (result_denominator / other.denominator) * other.numerator)

        result_numerator: int = first_numerator + second_numerator
        return Fraction(result_numerator, result_denominator)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Calculate the difference between the current fraction and other
        and returns the result as another fraction"""
        result_denominator: int = self.denominator * other.denominator

        # Get the numerator for the first fraction
        first_numerator: int = int(
            (result_denominator / self.denominator) * self.numerator)
        # Get the numerator for the second fraction
        second_numerator: int = int(
            (result_denominator / other.denominator) * other.numerator)

        result_numerator: int = first_numerator - second_numerator
        return Fraction(result_numerator, result_denominator)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Calculate the product between the current 
        fraction and the other fraction and returns the 
        result as another fraction"""
        result_numerator: int = self.numerator * other.numerator
        result_denominator: int = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Calculate the quotient between the current fraction and 
        the other fraction and returns the result as another fraction"""

        # We invert the numerator and denominator of other
        fraction = Fraction(other.denominator, other.numerator)

        # We use the times operation since is the same logic
        return self.__mul__(fraction)

    def __eq__(self, other: 'Fraction') -> bool:
        """Check if the two fractions are equal"""
        return (self.numerator * other.denominator) == (
                self.denominator * other.numerator)

    def __ne__(self, other: 'Fraction') -> bool:
        """Check if the two fractions are not equal"""
        return not self.__eq__(other)

    def __lt__(self, other: 'Fraction') -> bool:
        """Check if the fraction is less than other fraction"""
        return self.numerator / self.denominator < \
               other.numerator / other.denominator

    def __le__(self, other: 'Fraction') -> bool:
        """Check if the fraction is less than or equal to other fraction"""
        return self.numerator / self.denominator <= \
               other.numerator / other.denominator

    def __gt__(self, other: 'Fraction') -> bool:
        """Check if the fraction is greater than other fraction"""
        return self.numerator / self.denominator > \
               other.numerator / other.denominator

    def __ge__(self, other: 'Fraction') -> bool:
        """Check if the fraction is greater than or equal to other fraction"""
        return self.numerator / self.denominator >= \
               other.numerator / other.denominator

    def simplify(self) -> 'Fraction':
        factor: int = gcf(self.numerator, self.denominator)

        if factor == 1:
            return self

        return Fraction(int(self.numerator / factor),
                        int(self.denominator / factor))

    def reduce(self) -> str:
        """Reduce a fraction for readability
        
        I know it's not required but i receive instructions from my
        professor that i need to go the extra mile 😅 
        """

        # Check if numerator is 0
        if self.numerator == 0:
            return '0'

        # Check if the module is 0
        if self.numerator > self.denominator and \
                self.numerator % self.denominator == 0:
            return f'{int(self.numerator / self.denominator)}'

        if self.numerator == self.denominator:
            return '1'

        d = gcd(self.numerator, self.denominator)

        return f'{int(self.numerator / d)}/{int(self.denominator / d)} ' \
               f'({round(self.numerator / self.denominator, 3)})'

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'


class FractionCalculator:
    __slots__ = ['first_fraction', 'operation', 'second_fraction', 'result',
                 'separator']

    def __init__(self):
        """Initialize the fraction calculator in here we assign
        all the properties that are going to be used"""
        self.first_fraction: Fraction or None = None
        self.second_fraction: Fraction or None = None
        self.operation: str = ''
        self.result: Fraction or bool or None = None
        self.separator: str = '-------------------------'

    def execute(self) -> None:
        """It starts a fraction calculator"""
        clear_screen()
        print("Welcome to the fraction calculator! 👾")
        print(self.separator)
        print('Get information for the first fraction')
        self.first_fraction: Fraction = self.get_fraction()
        print(self.separator)
        print('Get Fraction Operation')
        self.operation: str = self.get_operation()
        print(self.separator)
        print('Get information for the second fraction')
        self.second_fraction: Fraction = self.get_fraction()

        """ When we are diving we are rotating numerator and 
        denominator this will throw an exception """
        msg: str = 'This operation generates a zero value denominator, ' \
                   'press Enter to try again '
        if self.operation == '/' and self.second_fraction.numerator == 0:
            input(msg)
            return self.execute()
        self.result = self.get_operation_result()
        self.display_result()

    @staticmethod
    def get_fraction() -> 'Fraction':
        """Get fraction from user input"""

        # Loops until it gets a valid value for the numerator
        while True:
            try:
                user_input: str = input('Insert fraction numerator: ')
                numerator: int = int(user_input)
            except ValueError:
                print('Please insert a valid number')
            else:
                break

        # Loops until it gets a valid value for the denominator
        while True:
            try:
                user_input = input('Insert fraction denominator: ')
                denominator: int = int(user_input)
                if denominator == 0:
                    raise ZeroDivisionError
            except ValueError:
                print('Please insert a valid number')
            except ZeroDivisionError:
                print("Fractions can't have zero denominator")
            else:
                break

        return Fraction(numerator, denominator)

    @staticmethod
    def get_operation() -> str:
        # Loops until it gets a valid operator
        while True:
            user_input: str = input(
                'Please insert a valid operation (+, -, *, /, ==): ')
            if user_input == '+' or user_input == '-' or user_input == '*' \
                    or user_input == '/' or user_input == '==':
                return user_input
            print('I SAID A VALID OPERATION!!! 😡')

    def get_operation_result(self) -> 'Fraction' or bool:
        """Receives two fractions and a operation to be performed

        Returns a Fraction or a boolean depending on the operation
        If an invalid operation is passed it raise an exception
        """
        first_fraction = self.first_fraction
        operation = self.operation
        second_fraction = self.second_fraction

        if operation == '+':
            return first_fraction.__add__(second_fraction)

        if operation == '-':
            return first_fraction.__sub__(second_fraction)

        if operation == '*':
            return first_fraction.__mul__(second_fraction)

        if operation == '/':
            return first_fraction.__truediv__(second_fraction)

        if operation == '==':
            return first_fraction.__eq__(second_fraction)

        raise Exception('Invalid operation')

    def display_result(self) -> None:
        """Display the program message"""
        clear_screen()
        first_fraction = self.first_fraction
        operation = self.operation
        second_fraction = self.second_fraction
        result = self.result
        # This only happens with the equal operation
        print(f'First Fraction: {first_fraction}')
        print(f'Operation: {operation}')
        print(f'Second Fraction: {second_fraction}')
        print('-------------------------')
        if type(result) is bool:
            if result:
                print(f'{first_fraction} and {second_fraction} are equal')
            else:
                print(f'{first_fraction} and {second_fraction} are not equal')
            return

        # In this part result can only be a Fraction
        print(
            f'{first_fraction} {operation} {second_fraction} = '
            f'{result.reduce()}')


def main() -> None:
    """Main program function"""
    fraction_calculator: FractionCalculator = FractionCalculator()
    fraction_calculator.execute()


def test_suite() -> None:
    """It runs the test suite"""
    clear_screen()
    separator = '\n---------------------------\n'
    print("Hello I'm a robot 🤖")
    print(
        "I will run a test suite to make sure that everything "
        "is working fine 👌")
    print(separator)
    print('TEST SUITE #1')
    first_fraction: Fraction = Fraction(1, 2)  # 1/2
    second_fraction: Fraction = Fraction(3, 4)  # 3/4
    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [5/4]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [-1/4]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [3/8]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [2/3]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [False]')

    print(separator)
    print('TEST SUITE #2')
    first_fraction = Fraction(1, 3)  # 1/3
    second_fraction = Fraction(1, 3)  # 1/3
    third_fraction: Fraction = Fraction(1, 3)  # 1/3

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}')
    print(f'Third fraction: {third_fraction}\n')
    fraction_sum: Fraction = first_fraction.__add__(second_fraction).__add__(
        third_fraction)
    print(
        f'{first_fraction} + {second_fraction} + {third_fraction} = '
        f'{fraction_sum.reduce()} [1]')
    fraction_sum = first_fraction.__add__(second_fraction).__sub__(
        third_fraction)
    print(
        f'{first_fraction} + {second_fraction} - {third_fraction} = '
        f'{fraction_sum.reduce()} [1/3]')
    fraction_sum = first_fraction.__mul__(second_fraction).__truediv__(
        third_fraction)
    print(
        f'{first_fraction} * {second_fraction} / {third_fraction} = '
        f'{fraction_sum.reduce()} [1/3]')
    fraction_sum = first_fraction.__mul__(second_fraction).__mul__(
        third_fraction)
    print(
        f'{first_fraction} * {second_fraction} * {third_fraction} = '
        f'{fraction_sum.reduce()} [1/27]')
    fraction_sum = first_fraction.__sub__(second_fraction).__sub__(
        third_fraction)
    print(
        f'{first_fraction} - {second_fraction} - {third_fraction} = '
        f'{fraction_sum.reduce()} [-1/3]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [True]')

    print(separator)
    print('TEST SUITE #3')
    first_fraction = Fraction(1, 4)  # 1/4
    second_fraction = Fraction(3, 4)  # 3/4

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [1]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [-1/2]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [3/16]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [1/3]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [False]')

    print(separator)
    print('TEST SUITE #4')
    first_fraction = Fraction(1, 2)  # 1/2
    second_fraction = Fraction(4, 4)  # 4/4

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [3/2]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [-1/2]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [1/2]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [1/2]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [False]')

    print(separator)
    print('TEST SUITE #5')
    first_fraction = Fraction(1, 2)  # 1/2
    second_fraction = Fraction(1, 2)  # 1/2

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [1]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [0]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [1/4]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [1]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [True]')

    print(separator)
    print('TEST SUITE #6')
    first_fraction = Fraction(4, 4)  # 4/4
    second_fraction = Fraction(1, 2)  # 1/2

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [3/2]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [1/2]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [1/2]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [2]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [False]')

    print(separator)
    print('TEST SUITE #7')
    first_fraction = Fraction(4, 4)  # 4/4
    second_fraction = Fraction(12, 8)  # 12/8

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [5/2]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [-1/2]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [3/2]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [2/3]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [False]')

    print(separator)
    print('TEST SUITE #8')
    first_fraction = Fraction(12, 8)  # 12/8
    second_fraction = Fraction(4, 4)  # 4/4

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [5/2]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [1/2]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [3/2]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [3/2]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [False]')

    print(separator)
    print('TEST SUITE #9')
    first_fraction = Fraction(12, 8)  # 12/8
    second_fraction = Fraction(3, 2)  # 4/4

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [3]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [0]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [9/4]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [1]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [True]')

    print(separator)
    print('TEST SUITE #10')
    first_fraction = Fraction(3, 2)  # 12/8
    second_fraction = Fraction(12, 8)  # 4/4

    print(f'First fraction: {first_fraction}')
    print(f'Second fraction: {second_fraction}\n')
    print(
        f'{first_fraction} + {second_fraction} = '
        f'{first_fraction.__add__(second_fraction).reduce()} [3]')
    print(
        f'{first_fraction} - {second_fraction} = '
        f'{first_fraction.__sub__(second_fraction).reduce()} [0]')
    print(
        f'{first_fraction} * {second_fraction} = '
        f'{first_fraction.__mul__(second_fraction).reduce()} [9/4]')
    print(
        f'{first_fraction} / {second_fraction} = '
        f'{first_fraction.__truediv__(second_fraction).reduce()} [1]')
    print(
        f'Is {first_fraction} equal to {second_fraction} ? '
        f'{first_fraction.__eq__(second_fraction)} [True]')


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
