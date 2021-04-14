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
from typing import List, Dict, Tuple, Set
from prettytable import PrettyTable
import instructor
from instructor import Instructors, Instructor
import student
from student import Students, Student
import grade
from grade import Grades, Grade


class University:
    # Handles the university repository functionality

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

        instructors: List[Instructor] = Instructors.from_file(
            self.instructors_path)
        students: List[Student] = Students.from_file(self.student_path)
        grades: List[Grade] = Grades.from_file(self.grades_path)

        self.instructors: Instructors = Instructors(instructors)
        self.students: Students = Students(students)
        self.grades: Grades = Grades(grades)
        self.__validate_data_integrity()

    def __validate_files(self) -> None:
        # Validates that the required files exist and add them to self
        students: str = os.path.join(self.directory, "students.txt")
        instructors: str = os.path.join(self.directory, "instructors.txt")
        grades: str = os.path.join(self.directory, "grades.txt")

        # Validate path exists
        if not os.path.exists(students):
            raise FileNotFoundError(f"the path {students} do not exist")

        if not os.path.exists(instructors):
            raise FileNotFoundError(f"the path {instructors} do not exist")

        if not os.path.exists(grades):
            raise FileNotFoundError(f"the path {grades} do not exist")

        # Validates the path are files
        student_path: Path = Path(students)
        instructors_path: Path = Path(instructors)
        grades_path: Path = Path(grades)
        if not student_path.is_file():
            raise IsADirectoryError(f"the path {students} is a directory")

        if not instructors_path.is_file():
            raise IsADirectoryError(f"the path {instructors} is a directory")

        if not grades_path.is_file():
            raise IsADirectoryError(f"the path {grades} is a directory")

        self.student_path = students
        self.instructors_path = instructors
        self.grades_path = grades

    def __validate_data_integrity(self) -> None:
        """Validate that all the professor and student reference exists"""
        for item in self.grades.all():
            self.instructors.get(instructor.GetBy.ID, item.professor_id)
            self.students.get(student.GetBy.ID, item.student_id)

    def get_instructors(self) -> List[Instructor]:
        # Return a list of all the instructors in the university
        return [item for _, item in self.instructors.all().items()]

    def get_students(self) -> List[Student]:
        # Return a list of all the students in the university
        return [item for _, item in self.students.all().items()]

    def get_grades(self) -> List[Grade]:
        # Return a list of all the grades in the university
        return self.grades.all()

    def get_student_summary(self) -> List[Tuple[str, str, List[str]]]:
        # Calculate the summary for students
        summary: List[Tuple[str, str, List]] = []

        for learner in self.get_students():
            courses: List[str] = [item.course for item in
                                  self.grades.get(grade.GetBy.STUDENT,
                                                  learner.cwid)]
            summary.append((learner.cwid, learner.name, sorted(courses)))

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
        for grd in self.grades.all():
            cwid: str = grd.professor_id
            if cwid not in instructor_dict:
                instructor_dict[cwid] = set([])

            courses: Set[str] = instructor_dict[cwid]
            courses.add(grd.course)

            instructor_dict[cwid] = courses

        for cwid, courses in instructor_dict.items():
            teacher: Instructor = self.instructors.get(
                instructor.GetBy.ID, cwid)
            for course in sorted(list(courses)):
                summary.append((
                    cwid,
                    teacher.name,
                    teacher.department,
                    course,
                    len(self.grades.get(grade.GetBy.COURSE, course))
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
