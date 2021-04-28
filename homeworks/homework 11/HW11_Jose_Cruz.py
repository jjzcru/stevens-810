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
from typing import List, Dict, Tuple, Set, Union, Optional
from prettytable import PrettyTable
import sqlite3
from sqlite3 import Error, Connection
import instructor
from instructor import Instructors, Instructor
import student
from student import Students, Student
import grade
from grade import Grades, Grade
import major
from major import Majors, Major, Course


class University:
    # Handles the university repository functionality
    conn: Optional[Connection] = None

    def __init__(self, db_path: str) -> None:
        # Initialize university repository
        if type(db_path) != str:
            raise TypeError("Value must be a str")

        # Verifies that the file exist
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"the path {db_path} do not exist")

        path: Path = Path(db_path)
        if not path.is_file():
            raise ValueError(f"the path {db_path} is not a file")

        self.conn = self.get_connection(db_path)
        self.instructors = Instructors(self.conn)
        self.students = Students(self.conn)
        self.majors = Majors(self.conn)
        self.grades = Grades(self.conn)

    def get_connection(self, db_path: str):
        # Get database connection
        self.conn: Optional[Connection] = None

        try:
            return sqlite3.connect(db_path)
        except Error as e:
            print("Error opening the database")
            print(e)
            raise e

    def __del__(self):
        # Gets called when the object is destructed
        # Cleans the database connection if exist
        if self.conn is not None:
            self.conn.close()

    def get_instructors(self) -> List[Instructor]:
        # Return a list of all the instructors in the university
        return [item for _, item in self.instructors.all().items()]

    def get_students(self) -> List[Student]:
        # Return a list of all the students in the university
        return [item for _, item in self.students.all().items()]

    def get_grades(self) -> List[Grade]:
        # Return a list of all the grades in the university
        return self.grades.all()

    def get_majors(self) -> Dict[str, Major]:
        # Return a list of all the majors
        return self.majors.all()

    def get_student_summary(self) -> List[Tuple[
        str,
        str,
        str,
        List[str],
        List[str],
        List[str],
        float]
    ]:
        # Calculate the summary for students
        summary: List[Tuple[
            str,
            str,
            str,
            List[str],
            List[str],
            List[str],
            float
        ]] = []

        for learner in self.get_students():
            courses: List[str] = [item.course for item in
                                  self.grades.get(grade.GetBy.STUDENT,
                                                  learner.cwid)
                                  if item.passed]

            gpa: float = self.grades.get_student_gpa(learner.cwid)
            # Get a list of all the courses from the major
            major_courses: List[Course] = self.majors.get(learner.major).courses

            # If filter to get all the required courses
            required_courses: List[Course] = [course for course in major_courses
                                              if course.is_required]

            # I transform them to a set so i can use set theory
            major_courses_set: Set[str] = set(
                [m.name for m in required_courses]
            )

            # Get a list of all the elective courses from the major
            elective_courses: List[Course] = [course for course in major_courses
                                              if not course.is_required]
            # I transform them to a set so i can use set theory
            elective_courses_set: Set[str] = set(
                [m.name for m in elective_courses]
            )

            # Transform all the completed course to a set
            completed_courses: Set[str] = set(courses)

            """
                Do a set difference between the major courses and the 
                completed courses to get what are the remaining courses
            """
            remaining_required_courses: Set[str] = \
                major_courses_set.difference(completed_courses)

            """
                If there is a difference between the remaining elective 
                and the total of elective in the major i know that at least
                one elective was chosen. In that case there are not more 
                pending elective.
            """
            remaining_elective: Set[str] = \
                elective_courses_set.difference(completed_courses)
            remaining_elective_courses: List[str] = list(remaining_elective) \
                if len(remaining_elective) == len(elective_courses_set) \
                else []

            summary.append((
                learner.cwid,
                learner.name,
                learner.major,
                list(sorted(completed_courses)),
                list(sorted(remaining_required_courses)),
                list(sorted(remaining_elective_courses)),
                gpa))

        return summary

    def get_major_summary(self) -> List[Tuple[str, List[str], List[str]]]:
        # Calculate the summary for majors
        majors: Dict[str, Major] = self.get_majors()

        return sorted([(
            m.name,
            sorted([course.name
                    for course in m.get_course(major.GetBy.TYPE, True)]),
            sorted([course.name
                    for course in m.get_course(major.GetBy.TYPE, False)])
        ) for k, m in majors.items()], key=lambda m: m[0], reverse=True)

    def display_student_summary(self) -> None:
        """Display the summary as a table"""
        table = PrettyTable()
        table.field_names = [
            "CWID",
            "Name",
            "Major",
            "Completed Courses",
            "Remaining Required",
            "Remaining Elective",
            "GPA"
        ]

        for cwid, name, m, courses, remaining_req, remaining_ele, gpa in \
                self.get_student_summary():
            table.add_row([
                cwid,
                name,
                m,
                courses,
                remaining_req,
                remaining_ele,
                round(gpa, 2)
            ])
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
        return sorted(summary, key=lambda x: x[0], reverse=True)

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

        summary: List[Tuple[str, str, str, str, int]] = \
            self.get_instructor_summary()

        for cwid, name, dept, course, students in summary:
            table.add_row([cwid, name, dept, course, students])
        print(table)

    def display_major_summary(self) -> None:
        """Display the summary as a table"""
        table = PrettyTable()
        table.field_names = [
            "Major",
            "Required courses",
            "Electives"
        ]

        for name, required_courses, optional_courses in \
                self.get_major_summary():
            table.add_row([name, required_courses, optional_courses])
        print(table)
