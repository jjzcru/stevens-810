"""
    Handles everything related to university students
"""
from collections import defaultdict
from typing import List, Optional, Dict, Union
from enum import Enum
from sqlite3 import Connection, Cursor, Row


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
    __slots__ = ["__students", "__conn"]
    __students: Dict[str, Student]

    def __init__(self, conn: Connection) -> None:
        # Initialize repository
        # Type validation
        if not isinstance(conn, Connection):
            raise TypeError("connection is not instance of Connection")

        self.__conn = conn

    def all(self) -> Dict[str, Student]:
        # Return all the instructors
        cursor: Cursor = self.__conn.cursor()
        cursor.execute("SELECT cwid, name, major FROM student ORDER BY cwid;")

        rows: List[Row] = cursor.fetchall()
        students: Dict[str, Student] = defaultdict()
        for row in rows:
            cwid: str = row[0]
            name: str = row[1]
            department: str = row[2]

            students[cwid] = Student(cwid, name, department)

        return students

    def get(self, by: GetBy, value: str) -> \
            Union[Student, List[Student]]:
        # Get student/s information depending on different criteria
        # Search a student by id
        cursor: Cursor = self.__conn.cursor()
        if by == GetBy.ID:
            cursor.execute("SELECT  cwid, name, major FROM student "
                           f"WHERE cwid = '{value}' LIMIT 1;")
            rows: List[Row] = cursor.fetchall()
            if len(rows) == 0:
                raise ValueError(f"student with cwid {value} do not exist")

            return Student(rows[0][0], rows[0][1], rows[0][2])

        # Get students by major
        if by == GetBy.MAJOR:
            cursor.execute("SELECT  cwid, name, major FROM student "
                           f"WHERE major = '{value}';")
            rows: List[Row] = cursor.fetchall()
            if len(rows) == 0:
                raise ValueError(f"student with cwid {value} do not exist")

            return [Student(row[0], row[1], row[2]) for row in rows]

        raise ValueError(f"{by} is not a supported get value")
