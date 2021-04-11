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
from typing import List, Optional, Dict, Tuple, Set
from prettytable import PrettyTable


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


class StudentRepository:
    # Process student information
    __slots__ = ["students"]
    students: Dict[str, Student]

    def __init__(self, students: List[Student]) -> None:
        # Initialize repository

        # Create a dictionary for the students
        records: Dict[str, Student] = defaultdict()
        for student in students:
            records[student.cwid] = student

        self.students = records

    def find_by_id(self, cwid: str) -> Optional[Student]:
        """Returns a student with the specified id throws an errors
        if do not exist"""
        student: Optional[Student] = self.students.get(cwid)
        if student is None:
            raise ValueError(f"student with cwid {cwid} do not exist")
        return student

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


class InstructorRepository:
    # Process instructor information
    __slots__ = ["instructors"]
    instructors: Dict[str, Instructor]

    def __init__(self, instructors: List[Instructor]) -> None:
        # Initialize repository

        # Create a dictionary for the instructors
        records: Dict[str, Instructor] = defaultdict()
        for instructor in instructors:
            records[instructor.cwid] = instructor

        self.instructors = records

    def find_by_id(self, cwid: str) -> Optional[Instructor]:
        """Returns a instructor with the specified id or throw an error if do
        not exist"""
        instructor: Optional[Instructor] = self.instructors.get(cwid)
        if instructor is None:
            raise ValueError(f"instructor with cwid {cwid} do not exist")
        return instructor

    def find_by_department(self, department: str) -> List[Instructor]:
        # Returns all the instructors that belongs to a specific department
        instructors: List[Instructor] = []
        for cwid in self.instructors:
            instructor: Instructor = self.instructors[cwid]
            if self.instructors[cwid].department == department:
                instructors.append(instructor)
        return instructors

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


class GradesRepository:
    # Represents grades repository
    __slots__ = ["grades"]

    def __init__(self, grades: List[Grade]) -> None:
        # Initialize the grade repository
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


class UniversityRepository:
    def __init__(self, directory: str) -> None:
        # Initialize university repository
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

        instructors: List[Instructor] = \
            InstructorRepository.from_file(self.instructors_path)
        students: List[Student] = \
            StudentRepository.from_file(self.student_path)
        grades: List[Grade] = \
            GradesRepository.from_file(self.grades_path)

        self.instructors_repository: InstructorRepository = \
            InstructorRepository(instructors)
        self.students_repository: StudentRepository = \
            StudentRepository(students)
        self.grades_repository: GradesRepository = \
            GradesRepository(grades)
        self.__validate_data_integrity()

    def __validate_files(self) -> None:
        # Validates that the required files exist and add them to self
        student: str = os.path.join(self.directory, "students.txt")
        instructors: str = os.path.join(self.directory, "instructors.txt")
        grades: str = os.path.join(self.directory, "grades.txt")

        # Validate path exists
        if not os.path.exists(student):
            raise FileNotFoundError(f"the path {student} do not exist")

        if not os.path.exists(instructors):
            raise FileNotFoundError(f"the path {instructors} do not exist")

        if not os.path.exists(grades):
            raise FileNotFoundError(f"the path {grades} do not exist")

        # Validates the path are files
        student_path: Path = Path(student)
        instructors_path: Path = Path(instructors)
        grades_path: Path = Path(grades)
        if not student_path.is_file():
            raise IsADirectoryError(f"the path {student} is a directory")

        if not instructors_path.is_file():
            raise IsADirectoryError(f"the path {instructors} is a directory")

        if not grades_path.is_file():
            raise IsADirectoryError(f"the path {grades} is a directory")

        self.student_path = student
        self.instructors_path = instructors
        self.grades_path = grades

    def __validate_data_integrity(self) -> None:
        """Validate that all the professor and student reference exists"""
        for grade in self.grades_repository.grades:
            self.instructors_repository.find_by_id(grade.professor_id)
            self.students_repository.find_by_id(grade.student_id)

    def get_student_summary(self) -> List[Tuple[str, str, List[str]]]:
        # Calculate the summary for students
        summary: List[Tuple[str, str, List]] = []
        for cwid, student in self.students_repository.students.items():
            courses: List[str] = [grade.course for grade in
                                  self.grades_repository.find_by_student(cwid)]
            courses.sort()
            summary.append((cwid, student.name, courses))

        return summary

    def display_student_summary(self) -> None:
        """Display the summary as a table"""
        table = PrettyTable()
        table.field_names = [
            "CWID",
            "Name",
            "Completed Courses",
        ]

        for cwid, name, courses in self.get_student_summary():
            table.add_row([cwid, name, courses])
        print(table)

    def get_instructor_summary(self) -> List[Tuple[str, str, str, str, int]]:
        # Calculate the instructor for instructors
        summary: List[Tuple[str, str, str, str, int]] = []
        instructor_dict: Dict[str, Set[str]] = defaultdict(set)
        for grade in self.grades_repository.grades:
            cwid: str = grade.professor_id
            if cwid not in instructor_dict:
                instructor_dict[cwid] = set([])

            courses: Set[str] = instructor_dict[cwid]
            courses.add(grade.course)

            instructor_dict[cwid] = courses

        for cwid, courses in instructor_dict.items():
            instructor: Instructor = \
                self.instructors_repository.find_by_id(cwid)

            for course in sorted(list(courses)):
                summary.append((
                    cwid,
                    instructor.name,
                    instructor.department,
                    course,
                    len(self.grades_repository.find_by_course(course))
                ))

        return summary

    def display_instructor_summary(self) -> None:
        """Display the summary as a table"""
        table = PrettyTable()
        table.field_names = [
            "CWID",
            "Name",
            "Dept",
            "Course",
            "Students"
        ]

        for cwid, name, dept, course, students in self.get_instructor_summary():
            table.add_row([cwid, name, dept, course, students])
        print(table)
