"""HW09: Repository

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
from typing import List


class Student:
    # Represents student object
    __slots__ = ['cwid', 'name', 'major']

    def __init__(self, cwid: str, name: str, major: str) -> None:
        # Initialize student object
        self.cwid = cwid
        self.name = name
        self.major = major


class Instructor:
    # Represents instructor object
    __slots__ = ['cwid', 'name', 'department']

    def __init__(self, cwid: str, name: str, department: str) -> None:
        # Initialize professor object
        self.cwid = cwid
        self.name = name
        self.department = department


class Grade:
    def __init__(self, student_id: str, course: str, grade: str,
                 professor_id: str) -> None:
        self.student_cwid = student_id
        self.course = course
        self.grade = grade
        self.professor_cwid = professor_id


class GradesRepository:
    def __init__(self, grades: List[Grade]) -> None:
        self.grades = grades

    @staticmethod
    def load(path: str) -> List[Grade]:

        grades: List[Grade] = []
        if type(path) != str:
            raise TypeError("path must be a str")

            # Verifies that the file exist
        if not os.path.exists(path):
            raise FileNotFoundError(f"the path {path} do not exist")

        if not Path(path).is_file():
            raise ValueError(f"the path {path} is not a file")

        line_counter: int = 0
        try:
            with open(path, "r") as file:
                for line in file.readlines():
                    line = line.strip('\n')
                    line_counter += 1

                    terms: List[str] = line.split('\t') if len(line) > 0 else []

                    if len(terms) != 4:
                        raise ValueError(
                            f"expect {4} fields but {len(terms)} were "
                            f"found")

                else:
                    file.close()
        except IOError as e:
            print(f'Error working with the file {path} \n{str(e)}')
        except ValueError as e:
            raise ValueError(
                f"Error in file '{path}' line {line_counter} \n{str(e)}")

        return grades


class UniversityRepository:
    def __init__(self, directory: str) -> None:
        if type(directory) != str:
            raise TypeError("Value must be a str")

            # Verifies that the file exist
        if not os.path.exists(directory):
            raise FileNotFoundError(f"the path {directory} do not exist")

        path: Path = Path(directory)
        if path.is_file():
            raise ValueError(f"the path {directory} is a file")

        self.directory = directory
        self.__validate_files()

    def __validate_files(self) -> None:
        # Validates that the required files exist and add them to self
        student: str = os.path.join(self.directory, "students.txt")
        instructors: str = os.path.join(self.directory, "instructors.txt")
        grades: str = os.path.join(self.directory, "grades.txt")

        # Validate path exists
        if not os.path.exists(student):
            raise FileNotFoundError(f'the path {student} do not exist')

        if not os.path.exists(instructors):
            raise FileNotFoundError(f'the path {instructors} do not exist')

        if not os.path.exists(grades):
            raise FileNotFoundError(f'the path {grades} do not exist')

        # Validates the path are files
        student_path: Path = Path(student)
        instructors_path: Path = Path(instructors)
        grades_path: Path = Path(grades)
        if not student_path.is_file():
            raise IsADirectoryError(f'the path {student} is a directory')

        if not instructors_path.is_file():
            raise IsADirectoryError(f'the path {instructors} is a directory')

        if not grades_path.is_file():
            raise IsADirectoryError(f'the path {grades} is a directory')

        self.__student_path = student
        self.__instructors_path = instructors
        self.__grades_path = grades
