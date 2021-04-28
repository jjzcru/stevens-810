"""
    Handles everything related to university grades
"""
from typing import List, Dict
from enum import Enum
from sqlite3 import Connection, Cursor, Row

grade_value_map: Dict[str, float] = {
    "A": 4.0,
    "A-": 3.75,
    "B+": 3.25,
    "B": 3.0,
    "B-": 2.75,
    "C+": 2.25,
    "C": 2.0,
    "C-": 0,
    "D+": 0,
    "D": 0,
    "D-": 0,
    "F": 0
}


class GetBy(Enum):
    # Enum for different ways to search
    STUDENT = 1
    INSTRUCTOR = 2
    COURSE = 3


class Grade:
    # Represents grade  object
    __slots__ = ["student_id", "course", "grade", "professor_id", "passed"]

    def __init__(self, student_id: str, course: str, grade: str,
                 professor_id: str) -> None:
        # Initialize grade object
        self.student_id = student_id
        self.grade = grade
        self.course = course
        self.professor_id = professor_id
        self.__validate()
        self.passed = grade_value_map[grade] > 0

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
    __slots__ = ["__grades", "__conn"]
    __grades: List[Grade]

    def __init__(self, conn: Connection) -> None:
        # Initialize repository
        # Type validation
        if not isinstance(conn, Connection):
            raise TypeError("connection is not instance of Connection")

        self.__conn = conn

    def all(self) -> List[Grade]:
        # Return all the instructors
        cursor: Cursor = self.__conn.cursor()
        cursor.execute("SELECT student_cwid, course, grade, instructor_cwid "
                       "FROM grade ORDER BY student_cwid;")

        rows: List[Row] = cursor.fetchall()
        return [Grade(row[0], row[1], row[2], row[3]) for row in rows]

    def get(self, by: GetBy, value: str) -> List[Grade]:
        # Get grades depending on different criteria
        query: str = "SELECT student_cwid, course, grade, instructor_cwid " \
                     "FROM grade "
        where: str = ""

        if by != GetBy.STUDENT and by != GetBy.INSTRUCTOR \
                and by != GetBy.COURSE:
            raise ValueError(f"{by} is not a supported get value")

        if by == GetBy.STUDENT:
            where = f"WHERE student_cwid = '{value}'"

        if by == GetBy.INSTRUCTOR:
            where = f"WHERE instructor_cwid = '{value}'"

        if by == GetBy.COURSE:
            where = f"WHERE course = '{value}'"

        cursor: Cursor = self.__conn.cursor()
        cursor.execute(query + where)

        rows: List[Row] = cursor.fetchall()
        return [Grade(row[0], row[1], row[2], row[3]) for row in rows]

    def get_student_gpa(self, cwid: str) -> float:
        # Function that receives an student cwid and return its GPA
        grades: List[Grade] = self.get(GetBy.STUDENT, cwid)
        # The student do not have any grade
        if len(grades) == 0:
            return 0

        # We get the value from the map and calculate the average
        return sum([
            grade_value_map[grade.grade]
            for grade in grades
        ]) / len(grades)