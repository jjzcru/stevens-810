"""
    Handles everything related to university instructors
"""

import os
from pathlib import Path
from collections import defaultdict
from typing import List, Optional, Dict, Union
from enum import Enum


class GetBy(Enum):
    # Enum for different ways to search
    ID = 1
    DEPARTMENT = 2


class Instructor:
    # Represents instructor object
    __slots__ = ["cwid", "name", "department"]

    def __init__(self, cwid: str, name: str, department: str) -> None:
        # Initialize instructor object
        self.cwid = cwid
        self.name = name
        self.department = department
        self.__validate()

    def __validate(self):
        # Validate input information
        if type(self.cwid) != str:
            raise TypeError("cwid must be a string")

        if len(self.cwid) == 0:
            raise ValueError("cwid can't be empty")

        if type(self.name) != str:
            raise TypeError("name must be a string")

        if len(self.name) == 0:
            raise ValueError("name can't be empty")

        if type(self.department) != str:
            raise TypeError("department must be a string")

        if len(self.department) == 0:
            raise ValueError("department can't be empty")


class Instructors:
    # Process instructor information
    __slots__ = ["__instructors"]
    __instructors: Dict[str, Instructor]

    def __init__(self, instructors: List[Instructor]) -> None:
        # Initialize repository
        # Type validation
        if not isinstance(instructors, List):
            raise TypeError("instructors is not instance of List")

        for instructor in instructors:
            if not isinstance(instructor, Instructor):
                raise TypeError("instructor is not instance of Instructor")

        # Create a dictionary for the instructors
        records: Dict[str, Instructor] = defaultdict()
        for instructor in instructors:
            records[instructor.cwid] = instructor

        self.__instructors = records

    def all(self) -> Dict[str, Instructor]:
        # Return all the instructors
        return self.__instructors

    def get(self, by: Optional[GetBy], value: Optional[str]) -> \
            Union[Instructor, List[Instructor]]:
        # Get instructor/s information depending on different criteria
        # Search a instructor by id
        if by == GetBy.ID:
            instructor: Optional[Instructor] = self.__instructors.get(value)
            if instructor is None:
                raise ValueError(f"instructor with cwid {value} do not exist")
            return instructor

        # Search a instructor by department
        instructors: List[Instructor] = []
        if by == GetBy.DEPARTMENT:
            for cwid in self.__instructors:
                instructor: Instructor = self.__instructors[cwid]
                if self.__instructors[cwid].department == value:
                    instructors.append(instructor)
            return instructors

        raise ValueError(f"{by} is not a supported get value")

    @staticmethod
    def from_file(file_path: str) -> List[Instructor]:
        # Get a list of instructors from a file
        instructors: List[Instructor] = []
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

                    # Skip empty lines
                    if len(line) == 0:
                        continue

                    terms: List[str] = line.split("\t") if len(line) > 0 else []

                    if len(terms) != 3:
                        raise ValueError(
                            f"expect {3} fields but {len(terms)} were found")

                    instructors.append(Instructor(terms[0], terms[1], terms[2]))
                else:
                    file.close()
        except IOError as e:
            print(f"Error working with the file {file_path} \n{str(e)}")
        except ValueError as e:
            raise ValueError(
                f"Error in file '{file_path}' line {line_counter} \n{str(e)}")

        return instructors
