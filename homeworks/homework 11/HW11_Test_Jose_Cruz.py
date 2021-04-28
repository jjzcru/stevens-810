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
        # Test getting a list of student from file
        non_existing_file_path: str = "./test"
        dir_path: str = "./support"
        file_path: str = "./support/grades.txt"

        with self.assertRaises(TypeError):
            Grades.from_file(0)

        with self.assertRaises(FileNotFoundError):
            Grades.from_file(non_existing_file_path)

        with self.assertRaises(ValueError):
            Grades.from_file(dir_path)

        grades: List[Grade] = \
            Grades.from_file(file_path, True)

        self.assertEqual(len(grades), 22)
        expected_result: List[Grade] = [
            Grade("10103", "SSW 567", "A", "98765"),
            Grade("10103", "SSW 564", "A-", "98764"),
            Grade("10103", "SSW 687", "B", "98764"),
        ]
        for i in range(len(grades[0:3])):
            self.assertEqual(grades[i].student_id,
                             expected_result[i].student_id)
            self.assertEqual(grades[i].course, expected_result[i].course)
            self.assertEqual(grades[i].grade, expected_result[i].grade)
            self.assertEqual(grades[i].professor_id,
                             expected_result[i].professor_id)

    def test_repository(self) -> None:
        # Test repository functionalities
        file_path: str = "./support/grades.txt"

        grades: List[Grade] = Grades.from_file(file_path, True)
        repository: Grades = Grades(grades)

        self.assertEqual(len(repository.all()), 22)
        self.assertEqual(len(repository.get(grade.GetBy.STUDENT, "10115")), 4)
        self.assertEqual(len(repository.get(grade.GetBy.STUDENT, "1011")), 0)
        self.assertEqual(len(repository.get(grade.GetBy.COURSE, "SSW 567")), 4)
        self.assertEqual(len(repository.get(grade.GetBy.COURSE, "SSW 999")), 0)
        self.assertEqual(len(
            repository.get(grade.GetBy.INSTRUCTOR, "98765")), 7)
        self.assertEqual(len(
            repository.get(grade.GetBy.INSTRUCTOR, "9876")), 0)


# TODO Fix this test
class MajorsTest(unittest.TestCase):
    """Test suite for Major"""

    def test_major(self) -> None:
        # Test grade object
        with self.assertRaises(TypeError):
            Major(0, 'Test', 'X')

        with self.assertRaises(ValueError):
            Major('', 'Test', 'test')

        with self.assertRaises(TypeError):
            Major('123', 'Test', [])

    def test_from_file(self) -> None:
        # Test getting a list of student from file
        non_existing_file_path: str = "./test"
        dir_path: str = "./support"
        file_path: str = "./support/majors.txt"

        with self.assertRaises(TypeError):
            Majors.from_file(0)

        with self.assertRaises(FileNotFoundError):
            Majors.from_file(non_existing_file_path)

        with self.assertRaises(ValueError):
            Majors.from_file(dir_path)

        majors: List[Major] = Majors.from_file(file_path, True)

        self.assertEqual(len(majors), 2)
        expected_result: List[Major] = [
            Major("SFEN", Course("SSW 540", True)),
        ]
        for i in range(len(majors[0:3])):
            self.assertEqual(majors[i].name,
                             expected_result[i].name)

    def test_repository(self) -> None:
        # Test repository functionalities
        file_path: str = "./support/majors.txt"

        majors: List[Major] = Majors.from_file(file_path, True)
        repository: Majors = Majors(majors)

        self.assertEqual(len(repository.all()), 13)
        self.assertEqual(len(repository.get(major.GetBy.MAJOR, "SFEN")), 7)
        self.assertEqual(len(repository.get(major.GetBy.MAJOR, "SYEN")), 6)

        self.assertEqual(len(repository.get(major.GetBy.FLAG, "R")), 7)
        self.assertEqual(len(repository.get(major.GetBy.FLAG, "E")), 6)

        self.assertEqual(len(repository.get(major.GetBy.COURSE, "SSW 540")), 2)
        self.assertEqual(len(repository.get(major.GetBy.COURSE, "SSW 810")), 1)


class UniversityTest(unittest.TestCase):
    """Test suite for University"""

    def test_init(self) -> None:
        # Test repository functionalities
        non_dir_path: str = "./support/instructors.txt"
        non_existing_dir_path: str = "./test"

        with self.assertRaises(TypeError):
            University(0)

        with self.assertRaises(FileNotFoundError):
            University(non_existing_dir_path)

        with self.assertRaises(ValueError):
            University(non_dir_path)

    def test_student_summary(self):
        dir_path: str = "./support"
        repository: University = University(dir_path)
        self.assertEqual(len(repository.get_students()), 10)
        summary: List[Tuple[str, str, List[str]]] = \
            repository.get_student_summary()
        self.assertEqual(len(summary), 10)
        # TODO Fix this validation
        """expected: List[Tuple[str, str, List[str]]] = [
            ("10103", "Baldwin, C", ["CS 501", "SSW 564", "SSW 567",
                                     "SSW 687"]),
            ("10115", "Wyatt, X", ["CS 545", "SSW 564", "SSW 567", "SSW 687"]),
            ("10172", "Forbes, I", ["SSW 555", "SSW 567"])
        ]
        for i in range(len(summary[0:3])):
            self.assertEqual(summary[i], expected[i])"""
        print('Student Summary')
        repository.display_student_summary()

    def test_instructor_summary(self):
        dir_path: str = "./support"
        repository: University = University(dir_path)
        summary: List[Tuple[str, str, str, str, int]] = \
            repository.get_instructor_summary()
        expected: List[Tuple[str, str, str, str, int]] = [
            ("98765", "Einstein, A", "SFEN", "SSW 540", 3),
            ("98765", "Einstein, A", "SFEN", "SSW 567", 4),
            ("98764", "Feynman, R", "SFEN", "CS 501", 1),

        ]
        self.assertEqual(len(repository.get_instructors()), 6)
        self.assertEqual(len(summary), 12)
        for i in range(len(summary[0:3])):
            self.assertEqual(summary[i], expected[i])
        print('Instructor Summary')
        repository.display_instructor_summary()

    # TODO Complete test
    def test_major_summary(self):
        dir_path: str = "./support"
        repository: University = University(dir_path)
        self.assertEqual(len(repository.get_majors()), 2)
        print('Majors Summary')
        repository.display_major_summary()


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
