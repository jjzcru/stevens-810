"""HW09: University Repository

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
from collections import defaultdict
from typing import List, Optional, Dict


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
    # Represents grade  object
    __slots__ = ['student_id', 'course', 'grade', 'professor_id']

    def __init__(self, student_id: str, course: str, grade: str,
                 professor_id: str) -> None:
        self.student_id = student_id
        self.grade = grade
        self.course = course
        self.professor_id = professor_id
        self.__validate()

    def __validate(self):
        # Validate input information
        if type(self.student_id) != str:
            raise TypeError('student_id must be a string')

        if type(self.course) != str:
            raise TypeError('course must be a string')

        if type(self.grade) != str:
            raise TypeError('grade must be a string')

        if type(self.professor_id) != str:
            raise TypeError('professor_id must be a string')

        if len(self.student_id) == 0:
            raise ValueError("student_id can't be empty")

        if len(self.course) == 0:
            raise ValueError("course can't be empty")

        if len(self.grade) == 0:
            raise ValueError("grade can't be empty")

        if len(self.professor_id) == 0:
            raise ValueError("professor_id can't be empty")

        self.grade = self.grade.upper()
        self.__validate_grade()

    def __validate_grade(self):
        grade: str = self.grade

        if grade != 'F' and \
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
            raise ValueError('Invalid grade letter')


class StudentRepository:
    # Process student information
    __slots__ = ['students']
    students: Dict[str, Student]

    def __init__(self, students: List[Student]) -> None:
        # Initialize repository

        # Create a dictionary for the students
        records: Dict[str, Student] = defaultdict()
        for student in students:
            records[student.cwid] = student

        self.students = records

    def find_by_id(self, cwid: str) -> Optional[Student]:
        # Returns a student with the specified id or None if do not exist
        return self.students.get(cwid)

    def find_by_major(self, major: str) -> List[Student]:
        # Returns all the students that belongs to a specific major
        students: List[Student] = []
        for cwid in self.students:
            student: Student = self.students[cwid]
            if self.students[cwid].major == major:
                students.append(student)
        return students

    @staticmethod
    def from_file(file_path: str) -> List[Student]:
        students: List[Student] = []
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
                    line = line.strip('\n')
                    line_counter += 1

                    # Skip empty lines
                    if len(line) == 0:
                        continue

                    terms: List[str] = line.split('\t') if len(line) > 0 else []

                    if len(terms) != 3:
                        raise ValueError(
                            f"expect {3} fields but {len(terms)} were found")

                    students.append(Student(terms[0], terms[1], terms[2]))
                else:
                    file.close()
        except IOError as e:
            print(f'Error working with the file {file_path} \n{str(e)}')
        except ValueError as e:
            raise ValueError(
                f"Error in file '{file_path}' line {line_counter} \n{str(e)}")

        return students


class InstructorRepository:
    # Process instructor information
    __slots__ = ['instructors']
    instructors: Dict[str, Instructor]

    def __init__(self, instructors: List[Instructor]) -> None:
        # Initialize repository

        # Create a dictionary for the students
        records: Dict[str, Instructor] = defaultdict()
        for instructor in instructors:
            records[instructor.cwid] = instructor

        self.instructors = records

    def find_by_id(self, cwid: str) -> Optional[Instructor]:
        # Returns a student with the specified id or None if do not exist
        return self.instructors.get(cwid)

    def find_by_department(self, department: str) -> List[Instructor]:
        # Returns all the students that belongs to a specific major
        instructors: List[Instructor] = []
        for cwid in self.instructors:
            instructor: Instructor = self.instructors[cwid]
            if self.instructors[cwid].department == department:
                instructors.append(instructor)
        return instructors

    @staticmethod
    def from_file(file_path: str) -> List[Instructor]:
        instructors: List[Instructor] = []
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
                    line = line.strip('\n')
                    line_counter += 1

                    # Skip empty lines
                    if len(line) == 0:
                        continue

                    terms: List[str] = line.split('\t') if len(line) > 0 else []

                    if len(terms) != 3:
                        raise ValueError(
                            f"expect {3} fields but {len(terms)} were found")

                    instructors.append(Instructor(terms[0], terms[1], terms[2]))
                else:
                    file.close()
        except IOError as e:
            print(f'Error working with the file {file_path} \n{str(e)}')
        except ValueError as e:
            raise ValueError(
                f"Error in file '{file_path}' line {line_counter} \n{str(e)}")

        return instructors


class GradesRepository:
    # Represents grades repository
    __slots__ = ['grades']

    def __init__(self, grades: List[Grade]) -> None:
        self.grades = grades

    def find_by_student(self, cwid: str) -> List[Grade]:
        # Returns all the grades from a student
        return [grade for grade in self.grades if grade.student_id == cwid]

    def find_by_instructor(self, cwid: str) -> List[Grade]:
        # Returns all the grades from a instructor
        return [grade for grade in self.grades if grade.professor_id == cwid]

    def find_by_course(self, course: str) -> List[Grade]:
        # Returns all the grades from a instructor
        return [grade for grade in self.grades if grade.course == course]

    @staticmethod
    def from_file(file_path: str) -> List[Grade]:
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
                    line = line.strip('\n')
                    line_counter += 1

                    # Skip empty lines
                    if len(line) == 0:
                        continue

                    terms: List[str] = line.split('\t') if len(line) > 0 else []

                    if len(terms) != 4:
                        raise ValueError(
                            f"expect {4} fields but {len(terms)} were found")

                    grades.append(Grade(terms[0], terms[1], terms[2], terms[3]))
                else:
                    file.close()
        except IOError as e:
            print(f'Error working with the file {file_path} \n{str(e)}')
        except ValueError as e:
            raise ValueError(
                f"Error in file '{file_path}' line {line_counter} \n{str(e)}")

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
