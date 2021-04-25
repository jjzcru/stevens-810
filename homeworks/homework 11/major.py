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
    NAME = 1
    TYPE = 2


class Course:
    # Represents major object
    __slots__ = ["name", "is_required"]

    def __init__(self, name: str, is_required: bool) -> None:
        # Initialize student object
        self.name = name
        self.is_required = is_required
        self.__validate()

    def __validate(self):
        # Validate input information
        if type(self.name) != str:
            raise TypeError("name must be a string")

        if len(self.name) == 0:
            raise ValueError("name can't be empty")

        if type(self.is_required) != bool:
            raise TypeError("is_required must be a bool")


class Major:
    # Represents major object
    __slots__ = ["name", "courses"]

    def __init__(self, name: str, courses: List[Course]) -> None:
        # Initialize student object
        self.name = name
        self.courses = courses
        self.__validate()

    def __validate(self):
        # Validate input information
        if type(self.name) != str:
            raise TypeError("name must be a string")

        if len(self.name) == 0:
            raise ValueError("name can't be empty")

        if not isinstance(self.courses, List):
            raise TypeError("majors is not instance of List")

        for course in self.courses:
            if not isinstance(course, Course):
                raise TypeError("course is not instance of Course")

    def get_course(self, by: Optional[GetBy], value: Union[str, bool]) -> \
            Union[Course, List[Course]]:
        # Get instructor/s information depending on different criteria
        # Search a instructor by id
        if by == GetBy.NAME:
            for course in self.courses:
                if course.name == value:
                    return course
            raise ValueError(f"course with name {value} do not exist")

        # Search a course by type
        if by == GetBy.TYPE:
            if type(value) != bool:
                raise TypeError(f"for {by} the value must be bool")

            return [course for course in self.courses if
                    course.is_required == value]

        raise ValueError(f"{by} is not a supported get value")


class Majors:
    # Process student information
    __slots__ = ["__majors"]
    __majors: Dict[str, Major]

    def __init__(self, majors: List[Major]) -> None:
        # Initialize repository
        # Type validation
        if not isinstance(majors, List):
            raise TypeError("majors is not instance of List")

        for major in majors:
            if not isinstance(major, Major):
                raise TypeError("major is not instance of Major")

        # Create a dictionary for the instructors
        records: Dict[str, Major] = defaultdict()
        for major in majors:
            records[major.name] = major

        self.__majors = records

    def all(self) -> List[Major]:
        # Return all the students
        return self.__majors

    def get(self, name: str) -> Major:
        major: Optional[Major] = self.__majors.get(name)
        if major is None:
            raise ValueError(f"major with name {name} do not exist")
        return major

    @staticmethod
    def from_file(file_path: str,
                  ignore_header: bool = False) -> List[Major]:
        # Get a list of instructors from a file
        majors: List[Major] = []
        if type(file_path) != str:
            raise TypeError("file_path must be a str")

        # Verifies that the file exist
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"the path {file_path} do not exist")

        if not Path(file_path).is_file():
            raise ValueError(f"the path {file_path} is not a file")

        line_counter: int = 0
        majors_dict: Dict[str, List[Course]] = defaultdict()
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

                    if terms[1] != "R" and terms[1] != "E":
                        raise ValueError(
                            f"{terms[1]} is an invalid flag value for course")

                    if majors_dict.get(terms[0]) is None:
                        majors_dict[terms[0]] = [Course(terms[2],
                                                        terms[1] == "R")]

                    majors_dict[terms[0]].append(Course(terms[2],
                                                        terms[1] == "R"))
                else:
                    file.close()
        except IOError as e:
            print(f"Error working with the file {file_path} \n{str(e)}")
        except ValueError as e:
            raise ValueError(
                f"Error in file '{file_path}' line {line_counter} \n{str(e)}")

        for name, courses in majors_dict.items():
            majors.append(Major(name, courses))

        return majors
