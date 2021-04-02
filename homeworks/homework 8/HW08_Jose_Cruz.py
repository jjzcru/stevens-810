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
from datetime import datetime, timedelta, date
from typing import Dict, Tuple, Iterator


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


def file_reader(path, fields, sep=',', header=False) -> Iterator[Tuple[str]]:
    """ Your docstring should go here for the description of the function."""
    pass  # implement your code here


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
