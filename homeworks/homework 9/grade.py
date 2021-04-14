"""
    Handles everything related to university grades
"""
import os
from pathlib import Path
from typing import List
from enum import Enum


class GetBy(Enum):
    # Enum for different ways to search
    STUDENT = 1
    INSTRUCTOR = 2
    COURSE = 3


class Grade:
    # Represents grade  object
    __slots__ = ["student_id", "course", "grade", "professor_id"]

    def __init__(self, student_id: str, course: str, grade: str,
                 professor_id: str) -> None:
        # Initialize grade object
        self.student_id = student_id
        self.grade = grade
        self.course = course
        self.professor_id = professor_id
        self.__validate()

    def __validate(self):
        # Validate input information
        if type(self.student_id) != str:
            raise TypeError("student_id must be a string")

        if len(self.student_id) == 0:
            raise ValueError("student_id can't be empty")

        if type(self.course) != str:
            raise TypeError("course must be a string")

        if len(self.course) == 0:
            raise ValueError("course can't be empty")

        if type(self.grade) != str:
            raise TypeError("grade must be a string")

        if len(self.grade) == 0:
            raise ValueError("grade can't be empty")

        if type(self.professor_id) != str:
            raise TypeError("professor_id must be a string")

        if len(self.professor_id) == 0:
            raise ValueError("professor_id can't be empty")

        self.grade = self.grade.upper()
        self.__validate_grade()

    def __validate_grade(self):
        # Validate that the grade is valid
        grade: str = self.grade

        if grade != "F" and \
                grade != "D-" and \
                grade != "D" and \
                grade != "D+" and \
                grade != "C-" and \
                grade != "C" and \
                grade != "C+" and \
                grade != "B-" and \
                grade != "B" and \
                grade != "B+" and \
                grade != "A-" and \
                grade != "A" and \
                grade != "A+":
            raise ValueError(f"the letter {grade} is an invalid grade")


class Grades:
    # Represents grades repository
    __slots__ = ["__grades"]
    __grades: List[Grade]

    def __init__(self, grades: List[Grade]) -> None:
        # Initialize the grade repository
        # Validate information
        if not isinstance(grades, List):
            raise TypeError("grades is not instance of List")

        for grade in grades:
            if not isinstance(grade, Grade):
                raise TypeError("grade is not instance of Grade")

        self.__grades = grades

    def all(self) -> List[Grade]:
        # Return all the grades
        return self.__grades

    def get(self, by: GetBy, value: str) -> List[Grade]:
        # Get grades depending on different criteria
        if by == GetBy.STUDENT:
            return [grade for grade in self.__grades if
                    grade.student_id == value]

        if by == GetBy.INSTRUCTOR:
            return [grade for grade in self.__grades if
                    grade.professor_id == value]

        if by == GetBy.COURSE:
            return [grade for grade in self.__grades if
                    grade.course == value]

        raise ValueError(f"{by} is not a supported get value")

    @staticmethod
    def from_file(file_path: str) -> List[Grade]:
        # Get a list of grades from a file
        grades: List[Grade] = []
        if type(file_path) != str:
            raise TypeError("path must be a str")

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

                    if len(terms) != 4:
                        raise ValueError(
                            f"expect {4} fields but {len(terms)} were found")

                    grades.append(Grade(terms[0], terms[1], terms[2], terms[3]))
                else:
                    file.close()
        except IOError as e:
            print(f"Error working with the file {file_path} \n{str(e)}")
        except ValueError as e:
            raise ValueError(
                f"Error in file '{file_path}' line {line_counter} \n{str(e)}")

        return grades
