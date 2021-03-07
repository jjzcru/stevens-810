"""HW04: Five part assignment

   Part 1: count_vowels(seq)
   Write a function count_vowels(s) that takes a string as an argument and
   returns the number of vowel

   Part 2: last_occurrence(target, sequence)
    Write a function last_occurrence that takes two arguments:
    1. target: A target item to find
    2. sequence: A sequence of values, e.g. a list is a sequence as is str.


   CONVENTIONS:
   - Max character limit per line 80
   - CapWords for class names
   - snake_case for variables and functions
   - asertEqual for arithmetics operators
   - assertIsNone for Optional validation

   Author: Jose J. Cruz
"""
import unittest
from typing import List, Any, Sequence, Optional


def count_vowels(word: str) -> int:
    """Receives a word and return the amount of vowels"""
    total_of_vowels: int = 0
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u']

    for letter in word.lower():
        if letter in vowels:
            total_of_vowels += 1

    return total_of_vowels


def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
    """Receives target to find an a sequence and returns the index of
    the item if found or None otherwise"""
    index: Optional[int] = None
    for offset, item in enumerate(sequence):
        if item == target:
            index = offset
    return index


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

        d = gcf(self.numerator, self.denominator)

        return f'{int(self.numerator / d)}/{int(self.denominator / d)} ' \
               f'({round(self.numerator / self.denominator, 3)})'

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'


class CountVowelsTest(unittest.TestCase):
    """Test suite for counting vowels"""

    def test_count_vowels(self) -> None:
        """Test count vowels function"""
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('HeLlO wOrLd'), 3)


class LastOccurrenceTest(unittest.TestCase):
    """Test suite for get the last occurrence of a target"""

    def test_last_occurrence(self) -> None:
        """Test get the last occurrence"""
        self.assertEqual(last_occurrence(33, [42, 33, 21, 33]), 3)
        self.assertEqual(last_occurrence(21, [42, 33, 21, 33]), 2)
        self.assertEqual(last_occurrence(42, [42, 33, 21, 33]), 0)
        self.assertIsNone(last_occurrence(55, [42, 33, 21, 33]))

    def test_last_occurrence_with_str(self) -> None:
        """Test get the last occurrence"""
        self.assertEqual(last_occurrence('P', 'Python'), 0)
        self.assertIsNone(last_occurrence('p', 'Python'))


class GCFTest(unittest.TestCase):
    """Test suite for getting the greatest common factor"""

    def test_gcf(self) -> None:
        """Test getting the greatest common factor"""
        self.assertEqual(gcf(2, 4), 2)
        self.assertEqual(gcf(3, 6), 3)
        self.assertEqual(gcf(9, 3), 3)
        self.assertEqual(gcf(2, 5), 1)
        self.assertEqual(gcf(7, 13), 1)


class SimplifyTest(unittest.TestCase):
    """Test suite for simplifying fractions"""

    def test_simplify(self) -> None:
        """Test simplify method for fractions"""
        self.assertEqual(str(Fraction(9, 27).simplify()), str(Fraction(1, 3)))
        self.assertEqual(str(Fraction(5, 10).simplify()), str(Fraction(1, 2)))
        self.assertEqual(str(Fraction(14, 7).simplify()), str(Fraction(2, 1)))
        self.assertEqual(str(Fraction(49, 7).simplify()), str(Fraction(7, 1)))
        self.assertEqual(str(Fraction(-49, 7).simplify()), str(Fraction(-7, 1)))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
