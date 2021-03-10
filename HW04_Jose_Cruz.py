"""HW04: Five part assignment

    Part 1: count_vowels(seq)
        Write a function count_vowels(s) that takes a string as an argument and
        returns the number of vowel

    Part 2: last_occurrence(target, sequence)
        Write a function last_occurrence that takes two arguments:
            1. target: A target item to find
            2. sequence: A sequence of values, e.g. a list is a
            sequence as is str.

    Part 3: Fraction.simplify()
        Extend your Fractions with a new method, Fraction.simplify() class
        from HW03 and add a new simplify(self) method that returns a new
        Fraction that is simplified or just returns a copy of self if self
        can’t be simplified

    Part 4: my_enumerate(seq)
        Write a generator,  my_enumerate(seq: Sequence[Any]) -> Iterator[Any]
        that provides the same functionality

    Part 5: random_integer_generator
        Write a generator random_integer_generator that returns a potentially
        infinite sequence of random integers between a min and max value.

   CONVENTIONS:
   - Max character limit per line 80
   - CapWords for class names
   - snake_case for variables and functions

   Author: Jose J. Cruz
   CWID: 10467076
"""
import random
from typing import List, Any, Sequence, Optional, Iterator


def count_vowels(word: str) -> int:
    """Receives a word and return the amount of vowels"""
    if type(word) != str:
        raise TypeError('Value must be a str')

    total_of_vowels: int = 0
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u']

    for letter in word.lower():
        if letter in vowels:
            total_of_vowels += 1

    return total_of_vowels


def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
    """Receives target to find an a sequence and returns the index of
    the item if found or None otherwise"""

    if not isinstance(sequence, Sequence):
        raise TypeError('Value must be a Sequence')

    index: Optional[int] = None
    for offset, item in enumerate(sequence):
        if item == target:
            index = offset
    return index


def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """Receives a sequence and returns the item and the index position"""
    if not isinstance(seq, Sequence):
        raise TypeError('Value must be a Sequence')

    index: int = 0
    for item in seq:
        yield index, item
        index += 1


def random_integer_generator(minimum: int, maximum: int) -> Iterator[int]:
    """Returns a potentially infinite sequence of random integers
    between a min and max value"""
    if not isinstance(minimum, int):
        raise TypeError('Value must be an int')

    if not isinstance(maximum, int):
        raise TypeError('Value must be an int')

    if minimum > maximum:
        raise ValueError('minimum number can not be larger than maximum')

    # Make it infinite
    while True:
        yield random.randint(minimum, maximum)


def find_target(target: int, minimum: int, maximum: int, max_attempts: int) -> \
        Optional[int]:
    """Takes a min and max value and read random values until it finds
    the target"""
    if not isinstance(target, int):
        raise TypeError('Value must be an int')

    if not isinstance(minimum, int):
        raise TypeError('Value must be an int')

    if not isinstance(maximum, int):
        raise TypeError('Value must be an int')

    if minimum > maximum:
        raise ValueError('minimum number can not be larger than maximum')

    if target < minimum or target > maximum:
        raise ValueError('target number is not in range')

    attempts: int = 1
    for item in random_integer_generator(minimum, maximum):
        if item == target:
            return attempts

        if attempts >= max_attempts:
            break

        attempts += 1

    return None
