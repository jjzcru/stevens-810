"""
    Handles everything related to university majors
"""
from collections import defaultdict
from typing import List, Optional, Dict, Union
from enum import Enum
from sqlite3 import Connection, Cursor, Row


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
        # Get majors/s information depending on different criteria
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
    # Process major information
    __slots__ = ["__majors", "__conn"]
    __majors: Dict[str, Major]

    def __init__(self, conn: Connection) -> None:
        # Initialize repository
        # Type validation
        if not isinstance(conn, Connection):
            raise TypeError("connection is not instance of Connection")

        self.__conn = conn

    def all(self) -> List[Major]:
        # Return all the instructors
        cursor: Cursor = self.__conn.cursor()
        cursor.execute("SELECT id FROM major ORDER BY id;")

        rows: List[Row] = cursor.fetchall()
        majors: Dict[str, Major] = defaultdict()
        for row in rows:
            major: str = row[0]
            courses: List[Course] = self.get_courses(major)
            majors[major] = Major(major, courses)

        return majors

    def get_courses(self, major: str) -> List[Course]:
        # Get a list of courses from a major
        cursor: Cursor = self.__conn.cursor()
        cursor.execute("SELECT id, flag FROM course "
                       f"WHERE major = '{major}' ORDER BY id;")

        rows: List[Row] = cursor.fetchall()
        return [Course(row[0], row[1] == "R") for row in rows]

    def get(self, name: str) -> Major:
        # Get a major by its name
        major: Optional[Major] = self.__majors.get(name)
        if major is None:
            raise ValueError(f"major with name {name} do not exist")

        return major
