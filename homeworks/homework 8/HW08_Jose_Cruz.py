"""HW08: Python parameters, modules, files, and the web

    Part 1: Date Arithmetic Operations
    Part 2: field separated file reader
    Part 3: Scanning directories and files
    
    CONVENTIONS:
        - Max character limit per line 80
        - CapWords for class names
        - snake_case for variables and functions
        - double quotes for strings

   Author: Jose J. Cruz
   CWID: 10467076
"""
import os
from pathlib import Path
from datetime import datetime, timedelta, date
from typing import Dict, Tuple, Iterator, List


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ Tuple that returns two datetime and one int.
        1. An instance of  class datetime representing the date three days
        after Feb 27, 2020.
        2. An instance of  class datetime representing the date three days
        after Feb 27, 2019.
        3. An int representing the number of days between
        Feb 1, 2019 and Sept 30, 2019
    ."""

    # Feb 27, 2020.
    first_input_date: datetime = datetime(2020, 2, 27)

    # Feb 27, 2019.
    second_input_date: datetime = datetime(2019, 2, 27)

    # Represents a difference of two days between dates
    days_delta: timedelta = timedelta(days=3)

    # Calculate the amount of days of difference between 2 date
    days_passed: int = (date(2019, 9, 30) - date(2019, 2, 1)).days

    return first_input_date + days_delta, \
           second_input_date + days_delta, \
           days_passed


def file_reader(path: str, fields: int, sep: str = ',', header: bool = False) \
        -> Iterator[List[str]]:
    """Return a generator using a file and split using separators"""
    # Performing type validation
    if type(path) != str:
        raise TypeError("Value must be a str")

    # Verifies that the file exist
    if not os.path.exists(path):
        raise FileNotFoundError(f'the path {path} do not exist')

    file_path = Path(path)
    if not file_path.is_file():
        raise IsADirectoryError(f'the path {path} is a directory')

    if type(fields) != int:
        raise TypeError("fields must be an int")

    if fields == 0:
        raise TypeError("fields must be bigger than 0")

    if type(sep) != str:
        raise TypeError("sep must be a str")

    if len(sep) == 0:
        raise ValueError("sep can't be empty")

    if type(header) != bool:
        raise TypeError("header must be a bool")

    line_counter: int = 0
    try:
        with open(path, "r") as file:
            for line in file.readlines():
                line = line.strip('\n')
                line_counter += 1
                if len(line) == 0:
                    raise ValueError(f"line {line_counter} is empty")

                terms: List[str] = line.split(sep)

                if len(terms) != fields:
                    raise ValueError(f"expect {fields} but {len(terms)} were "
                                     f"found")

                if header and line_counter == 1:
                    continue

                yield terms
            else:
                file.close()
    except IOError as e:
        print(f'Error working with the file {file_path} \n{str(e)}')
    except ValueError as e:
        raise ValueError(
            f"Error in file '{file_path}' line {line_counter} \n{str(e)}")


class FileAnalyzer:
    """ Your docstring should go here for the description of the class."""

    def __init__(self, directory: str) -> None:
        """ Your docstring should go here for the description of the method."""
        self.directory: str = directory  # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()

        self.analyze_files()  # summerize the python files data

    def analyze_files(self) -> None:
        """ Your docstring should go here for the description of the method."""
        pass  # implement your code here

    def pretty_print(self) -> None:
        """ Your docstring should go here for the description of the method."""
        pass  # implement your code here
