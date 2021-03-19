"""HW06: Lists, Tuples and Sets

    Part 1: list_copy(l: List[Any]) -> List[Any]
        Write a function list_copy(l) that takes a list as a parameter and
        returns a copy of the list using a list comprehension.

    Part 2: list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]
        Write a function that takes two lists as parameters and returns a new
        list with the values that are included in both lists.

    Part 3: list_difference(l1: List[Any], l2: List[Any]) -> List[Any]
        Write a function list_difference(l1, l2) that takes two lists as
        parameters and returns a new list with the values that are  in l1,
        but NOT in l2.

    Part 4: remove_vowels(string: str) -> str
        Write a function that given a string, splits the string on whitespace
        into words and returns a new string that includes only the words that
        do NOT begin with vowels.

   CONVENTIONS:
   - Max character limit per line 80
   - CapWords for class names
   - snake_case for variables and functions
   - function that start with underscore are private
   - double quotes for strings

   Author: Jose J. Cruz
   CWID: 10467076
"""
from typing import List, Any


def list_copy(input_list: List[any]) -> List[Any]:
    """Functions receives a list an return a copy"""
    if not isinstance(input_list, List):
        raise TypeError("input_list is not instance of List")

    return [item for item in input_list]


def list_intersect(first_list: List[Any], second_list: List[Any]) -> List[Any]:
    """Receives two list and return a new list with the intersected values"""
    if not isinstance(first_list, List):
        raise TypeError("first_list is not instance of List")

    if not isinstance(second_list, List):
        raise TypeError("second_list is not instance of List")

    """
        1. Transform list into a set, to get unique elements and also do not
        modify the original list
        2. We do an union operation to combine them
        3. We transform the set back to a list
    """

    combined_list: List[Any] = list(set(first_list) | set(second_list))

    # In the if segment we ask for items that exist in both lists
    return [item for item in combined_list if item in first_list
            and item in second_list]


def list_difference(first_list: List[Any], second_list: List[Any]) -> List[Any]:
    """Receives two list and return the items that exist in the first list
    that do not exist in the second list"""
    if not isinstance(first_list, List):
        raise TypeError("first_list is not instance of List")

    if not isinstance(second_list, List):
        raise TypeError("second_list is not instance of List")

    return [item for item in first_list if item not in second_list]


def remove_vowels(string: str) -> str:
    """Receive a string and return only words that do not start with a vowel"""
    vowels: List[str] = ["a", "e", "i", "o", "u"]
    if type(string) != str:
        raise TypeError("string must be a str")

    words: List[str] = string.split()

    return ' '.join([word for word in words if word[0].lower() not in vowels])
