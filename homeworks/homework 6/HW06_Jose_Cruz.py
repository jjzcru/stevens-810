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

    Part 5: check_pwd(password: str) -> bool
        Write a function that takes a string and return a bool

        The following conditions needs to be met:
            - The password includes at least two upper case characters
            - The password includes at least one lower case characters
            - The password starts with at least one digit

    Part 6: The DonutQueue
        Tracks customers as they arrive at the donut shop.
        Customers are added to the queue so they can be served in the order
        they arrived with the exception that priority customers are served
        before non-priority customers.

        Priority customers are served in the order they arrive,
        but before any non-priority customers

    Optional Practice Problem: reorder(l: List[Any]) -> List[Any]


   CONVENTIONS:
   - Max character limit per line 80
   - CapWords for class names
   - snake_case for variables and functions
   - function that start with underscore are private
   - double quotes for strings

   Author: Jose J. Cruz
   CWID: 10467076
"""
from typing import List, Any, Optional, Callable


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


def check_pwd(password: str) -> bool:
    """ Receive a string password and return a boolean depending if is valid
    or not.

    The following conditions needs to be met to be valid:
        - The password starts with at least one digit
        - The password includes at least two upper case characters
        - The password includes at least one lower case characters
    """
    if type(password) != str:
        raise TypeError("password must be a str")

    # The password requires at least 4 character in total
    if len(password) < 4:
        return False

    # Check if the first letter is a digit
    if not password[0].isdigit():
        return False

    # Check if there is at least 2 upper case
    if len([letter for letter in password if letter.isupper()]) < 2:
        return False

    # Check if there is at least 1 lower case
    if len([letter for letter in password if letter.islower()]) < 1:
        return False

    # If it reaches this point it mean that all the conditions are met
    return True


class Costumer:
    __slots__ = ['name', 'vip']
    """
        Represents a costumer in the Donut queue
    """

    def __init__(self, name: str, vip: bool = False):
        if type(name) != str:
            raise TypeError("name must be a str")

        if len(name) == 0:
            raise ValueError("name can't be empty")

        if type(vip) != bool:
            raise TypeError("vip must be a bool")

        self.name = name
        self.vip = vip


class DonutQueue:
    __slots__ = ['queue']
    """
        Tracks customers as they arrive at the donut shop.
        Customers are added to the queue so they can be served in the order
        they arrived with the exception that priority customers are served
        before non-priority customers.

        Priority customers are served in the order they arrive,
        but before any non-priority customers
        
        CONVENTION:
        - Next costumers comes from the last position of the list by using 
        pop() 
        - New customers are being inserted at the beginning in the list
        
        Meaning:
        - [0] = Last costumer in the queue 
        - [len(queue - 1)] = Next costumer in the queue 
    """
    queue: List[Costumer]

    def __init__(self):
        self.queue = []

    def arrive(self, name: str, vip: bool) -> None:
        """ Add a new costumer to the queue """
        costumer: Costumer = Costumer(name, vip)

        # If the queue is empty or the costumer is not vip we just put them
        # at the first position in the list
        if len(self.queue) == 0 or not costumer.vip:
            self.queue.insert(0, costumer)
            return

        next_position: int = self._next_vip_index()
        if next_position < 0:
            # There are no vip in the line so we just put them at the front
            self.queue.append(costumer)
            return

            # We put the vip in the same position as the last vip
        self.queue.insert(next_position, costumer)

    def next_customer(self) -> Optional[str]:
        """ Returns the costumer in the last position of the list"""
        if len(self.queue) == 0:
            return None

        return self.queue.pop().name

    def _next_vip_index(self) -> int:
        """ Returns the index of the next vip costumer or -1 if not found"""
        for index, costumer in enumerate(self.queue):
            if costumer.vip:
                return index
        return -1

    def waiting(self) -> Optional[str]:
        """
            Returns a comma separated string with the names of the customers
            waiting in the order they will be served or None if there are
            no customers waiting.
        """
        if len(self.queue) == 0:
            return None

        # Since we use the last position to get the next costumer
        # We reverse the list for printing purposes
        # The list is clone to not modify the original list
        queue: List[Costumer] = self.queue.copy()
        queue.reverse()

        return ', '.join(map(lambda costumer: costumer.name, queue))


def reorder(input_list: List[Any]) -> List[Any]:
    """ Use insertion sort to sort an incoming list """
    if not isinstance(input_list, List):
        raise TypeError("input_list is not instance of List")
    sorted_list: List[Any] = []
    for item in input_list:
        for index, sorted_item in enumerate(sorted_list):
            if sorted_item > item:
                sorted_list.insert(index, item)
                break
        else:
            sorted_list.append(item)
    return sorted_list
