"""HW05: String methods, slices, working with files, and automated testing

    Part 1: reverse(string)
        Function that takes a string as an argument and returns a new string
        which is the reverse of the argument.

    Part 2: substring(target: str, s: str) -> int
        Function that is similar to Python’s string.find(target) method
        that returns the offset from the beginning of  string s where target
        occurs in s.  Return -1 if target is not a substring in s.

    Part 3: find_second(target: str, string: str) -> int
        Function that is similar to Python’s string.find(target) method
        that returns the offset from the beginning of  string s where target
        occurs in s.  Return -1 if target is not a substring in s.

    Part 4: get_lines(path: str) -> Iterator[str]
        Function that is similar to Python’s string.find(target) method
        that returns the offset from the beginning of  string s where target
        occurs in s.  Return -1 if target is not a substring in s.

    Part 5: Write human readable code
        Be sure your code includes docstrings and follows the PEP-8 coding
        guidelines, e.g. CamelCase only for class names, appropriate spaces,
        etc.

        Insure that all of your functions include type hints for parameters
        and return types.  Be sure to include type hints for all variables.

        Provide adequate unittest test cases to demonstrate that your
        functions work properly.

   CONVENTIONS:
   - Max character limit per line 80
   - CapWords for class names
   - snake_case for variables and functions
   - function that start with underscore are private

   Author: Jose J. Cruz
   CWID: 10467076
"""
from typing import List, Iterator
from pathlib import Path
import os.path


def _find_nth_occurrence(target: str,
                         word: str,
                         occurrence_position: int = 1) -> int:
    """Find the n position for the occurrence for the target word"""

    # Performing type validation
    if type(target) != str:
        raise TypeError("Value must be a str")

    if type(word) != str:
        raise TypeError("Value must be a str")

    if type(occurrence_position) != int:
        raise TypeError("Value must be an int")

    # Validate the occurrence position is bigger than 1 (1 = first)
    if occurrence_position < 1:
        raise ValueError('Occurrence must be bigger or equal than one')

    # The target is bigger than the word so it will never be found
    if len(target) > len(word):
        return -1

    # Both have the same length meaning the only way to success is
    # if both are the same word in which case the result would be 0
    if len(target) == len(word):
        if target == word:
            return 0
        return -1

    # Store all the offsets found in the string
    founds: List[int] = []

    for offset in range(len(word) - len(target) + 1):
        substr: str = word[offset:(len(target) + offset)]
        if substr == target:
            founds.append(offset)

    for index, offset in enumerate(founds):
        if index + 1 == occurrence_position:
            return offset
    return -1


def reverse(word: str) -> str:
    """Receives a string and return the reverse word"""
    if type(word) != str:
        raise TypeError("Value must be a str")

    reverse_string: str = ""
    index: int = len(word)
    while index > 0:
        reverse_string += word[index - 1]
        index -= 1

    return reverse_string


def substring(target: str, word: str) -> int:
    """Returns the first offset from the beginning of string word
     where target occurs in word."""
    return _find_nth_occurrence(target, word)


def find_second(target: str, word: str) -> int:
    """Returns the second offset from the beginning of string word
         where target occurs in word."""
    return _find_nth_occurrence(target, word, 2)


def _remove_comments(line: str) -> str:
    comment_index = _find_nth_occurrence('#', line)
    if comment_index < 0:
        return line.strip('\n')

    if comment_index == 0:
        return ''

    response: str = line[0:comment_index]

    return response.strip('\n')


def get_lines(path: str) -> Iterator[str]:
    """Find the n position for the occurrence for the target word"""

    # Performing type validation
    if type(path) != str:
        raise TypeError("Value must be a str")

    # Verifies that the file exist
    if not os.path.exists(path):
        raise FileNotFoundError(f'the path {path} do not exist')

    file_path = Path(path)
    if not file_path.is_file():
        raise IOError(f'the path {path} is not a file')

    response: str = ''
    with open(path, "r") as file:
        for line in file.readlines():
            # Remove break lines
            line = line.strip('\n')

            # Ignores empty lines
            if len(line) == 0:
                continue

            # Trigger append and go to next iteration
            if line[-1] == '\\':
                line = line.strip('\\')
                response += line
                continue
            else:
                response += line

            # Remove comments
            response = _remove_comments(response)

            if len(response) > 0:
                # Yield the text and reset response
                yield response
                response = ''

        # If we have any remaining string in response we yield it
        # Example dangling \ characters
        if len(response) > 0:
            yield response

        # Make sure to close the file
        file.close()
