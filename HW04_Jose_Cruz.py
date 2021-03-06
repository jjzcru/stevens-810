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


class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self) -> None:
        """Test count vowels function"""
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('HeLlO wOrLd'), 3)


class LastOccurrenceTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
