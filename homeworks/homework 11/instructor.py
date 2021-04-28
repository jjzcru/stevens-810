"""
    Handles everything related to university instructors
"""

import os
from pathlib import Path
from collections import defaultdict
from typing import List, Optional, Dict, Union
from enum import Enum
from sqlite3 import Connection, Cursor, Row


class GetBy(Enum):
    # Enum for different ways to search
    ID = 1
    DEPARTMENT = 2


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


class Instructors:
    # Process instructor information
    __slots__ = ["__instructors", "__conn"]
    __instructors: Dict[str, Instructor]

    def __init__(self, conn: Connection) -> None:
        # Initialize repository
        # Type validation
        if not isinstance(conn, Connection):
            raise TypeError("connection is not instance of Connection")

        self.__conn = conn

    def all(self) -> List[Instructor]:
        cursor: Cursor = self.__conn.cursor()
        cursor.execute("SELECT cwid, name, department FROM instructor "
                       "ORDER BY cwid;")

        rows: List[Row] = cursor.fetchall()

        return [Instructor(row[0], row[1], row[2]) for row in rows]

    def get(self, by: Optional[GetBy], value: Optional[str]) -> \
            Union[Instructor, List[Instructor]]:
        # Get instructor/s information depending on different criteria
        # Search a instructor by id
        cursor: Cursor = self.__conn.cursor()
        if by == GetBy.ID:
            cursor.execute("SELECT cwid, name, department FROM instructor "
                           f"WHERE cwid = '{value}' LIMIT 1;")
            rows: List[Row] = cursor.fetchall()
            if len(rows) == 0:
                raise ValueError(f"instructor with cwid {value} do not exist")

            return Instructor(rows[0][0], rows[0][1], rows[0][2])

        # Search a instructor by department
        if by == GetBy.DEPARTMENT:
            cursor.execute("SELECT cwid, name, department FROM instructor "
                           f"WHERE department = '{value}';")
            rows: List[Row] = cursor.fetchall()
            if len(rows) == 0:
                raise ValueError(f"instructor with cwid {value} do not exist")

            return [Instructor(row[0], row[1], row[2]) for row in rows]

        raise ValueError(f"{by} is not a supported get value")
