"""HW07: Python Containers

    Part 1: Anagrams
        Part 1.1: Using strings and lists
        Part 1.2: Using dictionaries
        Part 1.3: Using Counters
    Part 2: Covers Alphabet
    Part 3: Web Analyzer
    
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
from typing import Dict, List, Tuple, Set


def anagrams_lst(first_word: str, second_word: str) -> bool:
    """Functions returns True if the strings are anagram and
    False if not (using list)"""
    if type(first_word) != str:
        raise TypeError("first_word must be a str")

    if type(second_word) != str:
        raise TypeError("second_word must be a str")

    if len(first_word) == 0 or len(second_word) == 0:
        raise ValueError("words can't be empty")

    first_word = first_word.lower().replace(" ", "")
    second_word = second_word.lower().replace(" ", "")

    for char in (first_word + second_word):
        if not char.isalpha():
            raise ValueError("numbers and symbols are not allowed")

    return sorted(list(first_word)) == sorted(list(second_word))


def anagrams_dd(first_word: str, second_word: str) -> bool:
    """Functions returns True if the strings are anagram and
    False if not (using dictionaries)"""
    if type(first_word) != str:
        raise TypeError("first_word must be a str")

    if type(second_word) != str:
        raise TypeError("second_word must be a str")

    if len(first_word) == 0 or len(second_word) == 0:
        raise ValueError("words can't be empty")

    first_word = first_word.lower().replace(" ", "")
    second_word = second_word.lower().replace(" ", "")

    for char in (first_word + second_word):
        if not char.isalpha():
            raise ValueError("numbers and symbols are not allowed")

    container: Dict[str, int] = defaultdict(int)

    for char in first_word:
        container[char] = container.get(char, 0) + 1

    for char in second_word:
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

    first_word = first_word.lower().replace(" ", "")
    second_word = second_word.lower().replace(" ", "")

    for char in (first_word + second_word):
        if not char.isalpha():
            raise ValueError("numbers and symbols are not allowed")

    return Counter(first_word) == Counter(second_word)


def covers_alphabet(sentence: str) -> bool:
    """Returns True if sentence includes at least one instance of every
    character in the alphabet or False using only Python sets"""
    if type(sentence) != str:
        raise TypeError("sentence must be a str")

    return set(''.join(filter(str.isalpha,
                              sentence.lower().replace(" ", "")))) == \
           set('abcdefghijklmnopqrstuvwxyz')


def hello(log):
    return log


def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """Create a summary of the weblogs with each distinct site and a sorted
    list of names of distinct people who visited that site"""

    # Defensive programming / Type checking section
    if not isinstance(weblogs, List):
        raise TypeError("weblogs is not instance of List")

    if len(weblogs) == 0:
        return []

    for weblog in weblogs:
        if not isinstance(weblog, Tuple):
            raise TypeError("log is not instance of Tuple")

        if len(weblog) != 2:
            raise ValueError("log can only have a length of two")

        if type(weblog[0]) != str or type(weblog[1]) != str:
            raise ValueError("log values must be strings")

    # Real Program
    records: Dict[str, Set] = defaultdict(set)
    list(map(lambda log: records[log[1]].add(log[0]), weblogs))
    return [(w, sorted(list(e))) for w, e in sorted(records.items())]
