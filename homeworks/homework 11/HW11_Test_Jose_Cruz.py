""" HW11: University Repository

    CONVENTIONS:
    - Max character limit per line 80
    - CapWords for class names
    - snake_case for variables and functions
    - double quotes for strings

   Author: Jose J. Cruz
   CWID: 10467076
"""
import unittest
from typing import List, Tuple, Dict
import sqlite3
from sqlite3 import Error, Connection
import instructor
from instructor import Instructors, Instructor
import student
from student import Students, Student
import grade
from grade import Grades, Grade
import major
from major import Major, Majors, Course
from HW11_Jose_Cruz import University


class InstructorsTest(unittest.TestCase):
    """Test suite for Instructor"""

    def test_from_file(self) -> None:
        # Test getting a list of instructors from sqlite
        db_path: str = "./db.sqlite"

        with self.assertRaises(TypeError):
            Instructors(0)

        with self.assertRaises(TypeError):
            Instructors(db_path)

        conn: Connection = sqlite3.connect(db_path)

        Instructors(conn)
        conn.close()

    def test_get_all(self) -> None:
        # Test repository functionalities
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Instructors = Instructors(conn)
        instructors: Dict[str, Instructor] = repository.all()
        self.assertEqual(len(instructors), 3)
        conn.close()

    def test_get_by_id(self) -> None:
        # Test get instructor by id
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Instructors = Instructors(conn)
        with self.assertRaises(ValueError):
            repository.get(instructor.GetBy.ID, "fff")

        teacher: Instructor = repository.get(instructor.GetBy.ID, "98762")
        self.assertEqual(teacher.cwid, "98762")
        self.assertEqual(teacher.name, "Hawking, S")
        self.assertEqual(teacher.department, "CS")
        conn.close()

    def test_get_by_department(self) -> None:
        # Test get instructor by department
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Instructors = Instructors(conn)
        instructors: List[Instructor] = \
            repository.get(instructor.GetBy.DEPARTMENT, "CS")

        self.assertEqual(len(instructors), 1)

        self.assertEqual(instructors[0].cwid, "98762")
        self.assertEqual(instructors[0].name, "Hawking, S")
        self.assertEqual(instructors[0].department, "CS")
        conn.close()


class StudentsTest(unittest.TestCase):
    """Test suite for Student"""

    def test_from_file(self) -> None:
        # Test getting a list of student from file
        db_path: str = "./db.sqlite"

        with self.assertRaises(TypeError):
            Students(0)

        with self.assertRaises(TypeError):
            Students(db_path)

        conn: Connection = sqlite3.connect(db_path)

        Students(conn)
        conn.close()

    def test_get_all(self) -> None:
        # Test repository functionalities
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Students = Students(conn)
        students: Dict[str, Student] = repository.all()
        self.assertEqual(len(students), 4)
        conn.close()

    def test_get_by_id(self) -> None:
        # Test get student by id
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Students = Students(conn)
        with self.assertRaises(ValueError):
            repository.get(student.GetBy.ID, "fff")

        learner: Student = repository.get(student.GetBy.ID, "10103")
        self.assertEqual(learner.cwid, "10103")
        self.assertEqual(learner.name, "Jobs, S")
        self.assertEqual(learner.major, "SFEN")
        conn.close()

    def test_get_by_major(self) -> None:
        # Test get instructor by department
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Students = Students(conn)
        students: List[Student] = \
            repository.get(student.GetBy.MAJOR, "CS")

        self.assertEqual(len(students), 1)

        self.assertEqual(students[0].cwid, "11714")
        self.assertEqual(students[0].name, "Gates, B")
        self.assertEqual(students[0].major, "CS")
        conn.close()


class MajorsTest(unittest.TestCase):
    """Test suite for Major"""

    def test_major(self) -> None:
        # Test major object
        with self.assertRaises(TypeError):
            Major(0, 'Test')

        with self.assertRaises(ValueError):
            Major('', 'Test')

        with self.assertRaises(TypeError):
            Major('123', 'Test')

    def test_from_file(self) -> None:
        # Test getting a list of student from file
        db_path: str = "./db.sqlite"

        with self.assertRaises(TypeError):
            Majors(0)

        with self.assertRaises(TypeError):
            Majors(db_path)

        conn: Connection = sqlite3.connect(db_path)

        Majors(conn)
        conn.close()

    def test_get_all(self) -> None:
        # Test repository functionalities
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Majors = Majors(conn)
        majors: List[Major] = repository.all()
        self.assertEqual(len(majors), 2)
        conn.close()


class GradesTest(unittest.TestCase):
    """Test suite for Grades"""

    def test_grade(self) -> None:
        # Test grade object
        with self.assertRaises(TypeError):
            Grade(0, 'Test', 'X', [])

        with self.assertRaises(ValueError):
            Grade('', 'Test', 'test', '12345')

        with self.assertRaises(ValueError):
            Grade('123', 'Test', 'X', '12345')

    def test_from_file(self) -> None:
        # Test getting a list of grades from db
        db_path: str = "./db.sqlite"

        with self.assertRaises(TypeError):
            Grades(0)

        with self.assertRaises(TypeError):
            Grades(db_path)

        conn: Connection = sqlite3.connect(db_path)

        Grades(conn)
        conn.close()

    def test_get_all(self) -> None:
        # Test repository functionalities
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Grades = Grades(conn)
        grades: List[Grade] = repository.all()
        self.assertEqual(len(grades), 9)
        conn.close()

    def test_get_by_student(self) -> None:
        # Get grades from student
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Grades = Grades(conn)
        grades: List[Grade] = repository.get(grade.GetBy.STUDENT, "10103")
        self.assertEqual(len(grades), 2)
        conn.close()

    def test_get_by_instructor(self) -> None:
        # Get grades from instructor
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Grades = Grades(conn)
        grades: List[Grade] = repository.get(grade.GetBy.INSTRUCTOR, "98763")
        self.assertEqual(len(grades), 5)
        conn.close()

    def test_get_by_course(self) -> None:
        # Get grades from course
        db_path: str = "./db.sqlite"
        conn: Connection = sqlite3.connect(db_path)

        repository: Grades = Grades(conn)
        grades: List[Grade] = repository.get(grade.GetBy.COURSE, "SSW 810")
        self.assertEqual(len(grades), 4)
        conn.close()


class UniversityTest(unittest.TestCase):
    """Test suite for University"""

    def test_init(self) -> None:
        # Test repository functionalities
        non_existing_dir_path: str = "./test"

        with self.assertRaises(TypeError):
            University(0)

        with self.assertRaises(FileNotFoundError):
            University(non_existing_dir_path)

    def test_student_summary(self):
        # Test student summary
        db_path: str = "./db.sqlite"
        repository: University = University(db_path)
        self.assertEqual(len(repository.get_students()), 4)
        summary: List[Tuple[str, str, List[str]]] = \
            repository.get_student_summary()
        self.assertEqual(len(summary), 4)
        print('Student Summary')
        repository.display_student_summary()

    def test_instructor_summary(self):
        # Test instructor summary
        db_path: str = "./db.sqlite"
        repository: University = University(db_path)
        summary: List[Tuple[str, str, str, str, int]] = \
            repository.get_instructor_summary()
        expected: List[Tuple[str, str, str, str, int]] = [
            ("98764", "Cohen, R", "SFEN", "CS 546", 2),
            ("98763", "Rowland, J", "SFEN", "SSW 555", 1),
            ("98763", "Rowland, J", "SFEN", "SSW 810", 4),
            ("98762", "Hawking, S", "CS", "CS 501", 1),
            ("98762", "Hawking, S", "CS", "CS 546", 2),
            ("98762", "Hawking, S", "CS", "CS 570", 1),
        ]
        self.assertEqual(len(summary), 6)
        for i in range(len(summary)):
            self.assertEqual(summary[i], expected[i])
        print('Instructor Summary')
        repository.display_instructor_summary()

    def test_major_summary(self):
        # Test major summary
        db_path: str = "./db.sqlite"
        repository: University = University(db_path)
        self.assertEqual(len(repository.get_majors()), 2)
        print('Majors Summary')
        repository.display_major_summary()


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
