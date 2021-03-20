# HW06
Lists, Tuples and Sets

**Author**: Jose J. Cruz

**CWID**: 10467076

## Parts
### Part 1: `list_copy(l: List[Any]) -> List[Any]`
Write a function list_copy(l) that takes a list as a parameter and
returns a copy of the list using a list comprehension.

### Part 2: `list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]`
Write a function that takes two lists as parameters and returns a new
list with the values that are included in both lists.

### Part 3: `list_difference(l1: List[Any], l2: List[Any]) -> List[Any]`
Write a function `list_difference(l1, l2)` that takes two lists as
parameters and returns a new list with the values that are  in l1,
but NOT in l2.

### Part 4: `remove_vowels(string: str) -> str`
Write a function that given a string, splits the string on whitespace
into words and returns a new string that includes only the words that
do NOT begin with vowels.

### Part 5: `check_pwd(password: str) -> bool`
Write a function that takes a string and return a bool

The following conditions needs to be met:
- The password includes at least two upper case characters
- The password includes at least one lower case characters
- The password starts with at least one digit

### Part 6: `DonutQueue`
 Tracks customers as they arrive at the donut shop.
Customers are added to the queue so they can be served in the order
they arrived with the exception that priority customers are served
before non-priority customers.

Priority customers are served in the order they arrive,
but before any non-priority customers

### Optional Practice Problem: `reorder(l: List[Any]) -> List[Any]`
Write a function `reorder(l: List[Any]) -> List[Any]` that returns a copy 
of the argument sorted using a list and the algorithm discussed in class. 

You MAY NOT simply use Python’s sort utilities. The idea is to start with an 
empty list, and then iterate through each of the elements in the list to be 
sorted, inserting each item in the proper spot in the new list.

## Conventions
- Max character limit per line 80
- CapWords for class names
- snake_case for variables and functions

## Unit Test
For run the unit test execute the following command
```
python HW06_Test_Jose_Cruz.py
```