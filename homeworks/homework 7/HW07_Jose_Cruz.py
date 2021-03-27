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


def anagrams_lst(first_word: str, second_word: str) -> bool:
    """Functions returns True if the strings are anagram and False if not"""
    if type(first_word) != str:
        raise TypeError("first_word must be a str")

    if type(second_word) != str:
        raise TypeError("second_word must be a str")

    if len(first_word) == 0 or len(second_word) == 0:
        raise ValueError("words can't be empty")

    return sorted(list(first_word.lower())) == sorted(list(second_word.lower()))
