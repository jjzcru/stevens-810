"""
    Handles everything related to university students
"""
import os
from pathlib import Path
from collections import defaultdict
from typing import List, Optional, Dict, Union
from enum import Enum


class GetBy(Enum):
    # Enum for different ways to search
    MAJOR = 1
    COURSE = 2
    FLAG = 3


class Major:
    # Represents major object
    __slots__ = ["name", "flag", "course"]

    def __init__(self, major: str, flag: str, course: str) -> None:
        # Initialize student object
        self.name = major
        self.flag = flag
        self.course = course
        self.__validate()

    def __validate(self):
        # Validate input information
        if type(self.name) != str:
            raise TypeError("name must be a string")

        if len(self.name) == 0:
            raise ValueError("name can't be empty")

        if type(self.flag) != str:
            raise TypeError("flag must be a string")

        if len(self.flag) == 0:
            raise ValueError("flag can't be empty")

        if type(self.course) != str:
            raise TypeError("course must be a string")

        if len(self.course) == 0:
            raise ValueError("course can't be empty")


class Majors:
    # Process student information
    __slots__ = ["__majors"]
    __majors: List[Major]

    def __init__(self, majors: List[Major]) -> None:
        # Initialize repository
        # Type validation
        if not isinstance(majors, List):
            raise TypeError("majors is not instance of List")

        for major in majors:
            if not isinstance(major, Major):
                raise TypeError("major is not instance of Major")

        # Create a dictionary for the students

        self.__majors = majors

    def all(self) -> List[Major]:
        # Return all the students
        return self.__majors

    def get(self, by: GetBy, value: str) -> List[Major]:
        # Get major/s information depending on different criteria
        if by == GetBy.MAJOR:
            return [major for major in self.__majors if
                    major.name == value]

        if by == GetBy.FLAG:
            return [major for major in self.__majors if
                    major.flag == value]

        if by == GetBy.COURSE:
            return [major for major in self.__majors if
                    major.course == value]

        raise ValueError(f"{by} is not a supported get value")

    @staticmethod
    def from_file(file_path: str, ignore_header: bool = False) -> List[Major]:
        # Get a list of students from a file
        # If ignore_header is True, it ignores the first line in the file
        majors: List[Major] = []
        if type(file_path) != str:
            raise TypeError("file_path must be a str")

        # Verifies that the file exist
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"the path {file_path} do not exist")

        if not Path(file_path).is_file():
            raise ValueError(f"the path {file_path} is not a file")

        line_counter: int = 0
        try:
            with open(file_path, "r") as file:
                for line in file.readlines():
                    line = line.strip("\n")
                    line_counter += 1
                    if ignore_header and line_counter == 1:
                        continue

                    # Skip empty lines
                    if len(line) == 0:
                        continue

                    terms: List[str] = line.split("\t") if len(line) > 0 else []

                    if len(terms) != 3:
                        raise ValueError(
                            f"expect {3} fields but {len(terms)} were found")

                    majors.append(Major(terms[0], terms[1], terms[2]))
                else:
                    file.close()
        except IOError as e:
            print(f"Error working with the file {file_path} \n{str(e)}")
        except ValueError as e:
            raise ValueError(
                f"Error in file '{file_path}' line {line_counter} \n{str(e)}")

        return majors
