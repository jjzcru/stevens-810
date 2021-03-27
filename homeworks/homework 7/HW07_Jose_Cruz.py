"""HW06: Lists, Tuples and Sets

    Part 1: Anagrams
    
    CONVENTIONS:
        - Max character limit per line 80
        - CapWords for class names
        - snake_case for variables and functions
        - function that start with underscore are private
        - double quotes for strings

   Author: Jose J. Cruz
   CWID: 10467076
"""
from collections import defaultdict, Counter
from typing import Dict


def anagrams_lst(first_word: str, second_word: str) -> bool:
    """Functions returns True if the strings are anagram and
    False if not (using list)"""
    if type(first_word) != str:
        raise TypeError("first_word must be a str")

    if type(second_word) != str:
        raise TypeError("second_word must be a str")

    if len(first_word) == 0 or len(second_word) == 0:
        raise ValueError("words can't be empty")

    return sorted(list(first_word.lower().replace(" ", ""))) == \
           sorted(list(second_word.lower().replace(" ", "")))


def anagrams_dd(first_word: str, second_word: str) -> bool:
    """Functions returns True if the strings are anagram and
    False if not (using dictionaries)"""
    if type(first_word) != str:
        raise TypeError("first_word must be a str")

    if type(second_word) != str:
        raise TypeError("second_word must be a str")

    if len(first_word) == 0 or len(second_word) == 0:
        raise ValueError("words can't be empty")

    container: Dict[str, int] = defaultdict(int)

    for char in first_word.lower().replace(" ", ""):
        container[char] = container.get(char, 0) + 1

    for char in second_word.lower().replace(" ", ""):
        container[char] = container.get(char, 0) - 1

    for char in container.keys():
        if container.get(char) != 0:
            return False

    return True


def anagrams_cntr(first_word: str, second_word: str) -> bool:
    """Functions returns True if the strings are anagram and
    False if not (using Counter)"""
    if type(first_word) != str:
        raise TypeError("first_word must be a str")

    if type(second_word) != str:
        raise TypeError("second_word must be a str")

    if len(first_word) == 0 or len(second_word) == 0:
        raise ValueError("words can't be empty")

    return Counter(first_word.lower().replace(" ", "")) == \
           Counter(second_word.lower().replace(" ", ""))


def covers_alphabet(sentence: str) -> bool:
    """Returns True if sentence includes at least one instance of every
    character in the alphabet or False using only Python sets"""
    if type(sentence) != str:
        raise TypeError("sentence must be a str")

    return set(''.join(filter(str.isalpha,
                              sentence.lower().replace(" ", "")))) == \
           set('abcdefghijklmnopqrstuvwxyz')
