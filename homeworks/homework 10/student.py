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
    ID = 1
    MAJOR = 2


class Student:
    # Represents student object
    __slots__ = ["cwid", "name", "major"]

    def __init__(self, cwid: str, name: str, major: str) -> None:
        # Initialize student object
        self.cwid = cwid
        self.name = name
        self.major = major
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

        if type(self.major) != str:
            raise TypeError("major must be a string")

        if len(self.major) == 0:
            raise ValueError("major can't be empty")


class Students:
    # Process student information
    __slots__ = ["__students"]
    __students: Dict[str, Student]

    def __init__(self, students: List[Student]) -> None:
        # Initialize repository
        # Type validation
        if not isinstance(students, List):
            raise TypeError("students is not instance of List")

        for student in students:
            if not isinstance(student, Student):
                raise TypeError("student is not instance of Student")

        # Create a dictionary for the students
        records: Dict[str, Student] = defaultdict()
        for student in students:
            records[student.cwid] = student

        self.__students = records

    def all(self) -> Dict[str, Student]:
        # Return all the students
        return self.__students

    def get(self, by: GetBy, value: str) -> \
            Union[Student, List[Student]]:
        # Get student/s information depending on different criteria
        # Search a student by id
        if by == GetBy.ID:
            student: Optional[Student] = self.__students.get(value)
            if student is None:
                raise ValueError(f"student with cwid {value} do not exist")
            return student

        # Get students by major
        instructors: List[Student] = []
        if by == GetBy.MAJOR:
            for cwid in self.__students:
                student: Student = self.__students[cwid]
                if self.__students[cwid].major == value:
                    instructors.append(student)
            return instructors

        raise ValueError(f"{by} is not a supported get value")

    @staticmethod
    def from_file(file_path: str) -> List[Student]:
        # Get a list of students from a file
        students: List[Student] = []
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

                    students.append(Student(terms[0], terms[1], terms[2]))
                else:
                    file.close()
        except IOError as e:
            print(f"Error working with the file {file_path} \n{str(e)}")
        except ValueError as e:
            raise ValueError(
                f"Error in file '{file_path}' line {line_counter} \n{str(e)}")

        return students
