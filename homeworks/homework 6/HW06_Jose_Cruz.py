"""HW06: Lists

    Part 1: list_copy(l: List[Any]) -> List[Any]
        Write a function list_copy(l) that takes a list as a parameter and
        returns a copy of the list using a list comprehension.

   CONVENTIONS:
   - Max character limit per line 80
   - CapWords for class names
   - snake_case for variables and functions
   - function that start with underscore are private

   Author: Jose J. Cruz
   CWID: 10467076
"""
from typing import List, Any


def list_copy(input_list: List[any]) -> List[Any]:
    """Functions receives a list an return a copy"""
    if not isinstance(input_list, List):
        raise TypeError('variable is not instance of List')

    return [item for item in input_list]
