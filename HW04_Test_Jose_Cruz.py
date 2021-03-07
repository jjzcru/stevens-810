"""HW04: Sequence, Iterators and Generators

    This class will test:
    - CountVowelsTest
    - LastOccurrenceTest
    - SimplifyTest
    - MyEnumerateTest
    - FindTargetTest

    CONVENTIONS:
    - Max character limit per line 80
    - CapWords for class names
    - snake_case for variables and functions
    - asertEqual for arithmetics operators
    - assertTrue for logical operators
    - assertRaises for test zero division
    - assertLessEqual for attempts validation

   Author: Jose J. Cruz
"""
import unittest
from HW03_Jose_Cruz import Fraction
from HW04_Jose_Cruz import count_vowels, last_occurrence, my_enumerate, \
    find_target


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


class SimplifyTest(unittest.TestCase):
    """Test suite for simplifying fractions"""

    def test_simplify(self) -> None:
        """Test simplify method for fractions"""
        self.assertEqual(str(Fraction(9, 27).simplify()), str(Fraction(1, 3)))
        self.assertEqual(str(Fraction(5, 10).simplify()), str(Fraction(1, 2)))
        self.assertEqual(str(Fraction(14, 7).simplify()), str(Fraction(2, 1)))
        self.assertEqual(str(Fraction(49, 7).simplify()), str(Fraction(7, 1)))
        self.assertEqual(str(Fraction(-49, 7).simplify()), str(Fraction(-7, 1)))


class MyEnumerateTest(unittest.TestCase):
    """Test suite for my enumerate implementation"""

    def test_my_enumerate(self) -> None:
        """Test my enumerate implementation"""
        self.assertEqual(list(my_enumerate([1, 2, 3])),
                         list(enumerate([1, 2, 3])))
        self.assertEqual(list(my_enumerate([3, 2, 1])),
                         list(enumerate([3, 2, 1])))
        self.assertEqual(list(my_enumerate([4, 4, 4, 4])),
                         list(enumerate([4, 4, 4, 4])))
        self.assertEqual(list(my_enumerate(['p', 'y', 't', 'h', 'o', 'n'])),
                         list(enumerate(['p', 'y', 't', 'h', 'o', 'n'])))
        self.assertEqual(list(my_enumerate([Fraction(1, 2), Fraction(3, 1)])),
                         list(enumerate([Fraction(1, 2), Fraction(3, 1)])))


class FindTargetTest(unittest.TestCase):
    """Test suite for finding target iterator"""

    def test_find_target_exception(self) -> None:
        """Test exception in find_target"""
        self.assertRaises(ValueError, find_target, 5, 7, 10, 100)
        self.assertRaises(ValueError, find_target, 5, 10, 1, 100)

    def test_find_target(self) -> None:
        """Test find target in generator"""
        self.assertLessEqual(find_target(3, 0, 10, 100), 100)
        self.assertIsNone(find_target(3, 0, 10000000, 1))
        self.assertLessEqual(find_target(2, 0, 20, 100000000), 100)
        self.assertLessEqual(find_target(2, 2, 2, 1), 1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
