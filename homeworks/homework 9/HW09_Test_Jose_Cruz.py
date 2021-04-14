"""HW05: University Repository

    CONVENTIONS:
    - Max character limit per line 80
    - CapWords for class names
    - snake_case for variables and functions
    - double quotes for strings

   Author: Jose J. Cruz
   CWID: 10467076
"""
import unittest
from typing import List, Tuple
import instructor
from instructor import Instructors, Instructor
import student
from student import Students, Student
import grade
from grade import Grades, Grade
from HW09_Jose_Cruz import University


class StudentsTest(unittest.TestCase):
    """Test suite for Students"""

    def test_from_file(self) -> None:
        # Test getting a list of student from file
        non_existing_file_path: str = "./test"
        dir_path: str = "./support"
        file_path: str = "./support/students.txt"

        with self.assertRaises(TypeError):
            Students.from_file(0)

        with self.assertRaises(FileNotFoundError):
            Students.from_file(non_existing_file_path)

        with self.assertRaises(ValueError):
            Students.from_file(dir_path)

        students: List[Student] = Students.from_file(file_path)

        self.assertEqual(len(students), 10)
        expected_result: List[Student] = [
            Student("10103", "Baldwin, C", "SFEN"),
            Student("10115", "Wyatt, X", "SFEN"),
            Student("10172", "Forbes, I", "SFEN"),
            Student("10175", "Erickson, D", "SFEN"),
            Student("10183", "Chapman, O", "SFEN"),
            Student("11399", "Cordova, I", "SYEN"),
            Student("11461", "Wright, U", "SYEN"),
            Student("11658", "Kelly, P", "SYEN"),
            Student("11714", "Morton, A", "SYEN"),
            Student("11788", "Fuller, E", "SYEN"),
        ]
        for i in range(len(students)):
            self.assertEqual(students[i].cwid, expected_result[i].cwid)
            self.assertEqual(students[i].name, expected_result[i].name)
            self.assertEqual(students[i].major, expected_result[i].major)

    def test_repository(self) -> None:
        # Test repository functionalities
        file_path: str = "./support/students.txt"

        students: List[Student] = Students.from_file(file_path)
        repository: Students = Students(students)

        self.assertEqual(len(repository.all()), 10)
        expected: Student = Student("10103", "Baldwin, C", "SFEN")

        learner: Student = repository.get(student.GetBy.ID, "10103")
        self.assertEqual(expected.cwid, learner.cwid)
        self.assertEqual(expected.name, learner.name)
        self.assertEqual(expected.major, learner.major)
        self.assertEqual(len(repository.get(student.GetBy.MAJOR, "SFEN")), 5)
        self.assertEqual(len(repository.get(student.GetBy.MAJOR, "SYEN")), 5)
        with self.assertRaises(ValueError):
            repository.get(student.GetBy.ID, "TEST")


class InstructorsTest(unittest.TestCase):
    """Test suite for Instructor"""

    def test_from_file(self) -> None:
        # Test getting a list of student from file
        non_existing_file_path: str = "./test"
        dir_path: str = "./support"
        file_path: str = "./support/instructors.txt"

        with self.assertRaises(TypeError):
            Instructors.from_file(0)

        with self.assertRaises(FileNotFoundError):
            Instructors.from_file(non_existing_file_path)

        with self.assertRaises(ValueError):
            Instructors.from_file(dir_path)

        instructors: List[Instructor] = \
            Instructors.from_file(file_path)

        self.assertEqual(len(instructors), 6)
        expected_result: List[Instructor] = [
            Instructor("98765", "Einstein, A", "SFEN"),
            Instructor("98764", "Feynman, R", "SFEN"),
            Instructor("98763", "Newton, I", "SFEN"),
            Instructor("98762", "Hawking, S", "SYEN"),
            Instructor("98761", "Edison, A", "SYEN"),
            Instructor("98760", "Darwin, C", "SYEN"),

        ]
        for i in range(len(instructors)):
            self.assertEqual(instructors[i].cwid, expected_result[i].cwid)
            self.assertEqual(instructors[i].name, expected_result[i].name)
            self.assertEqual(instructors[i].department,
                             expected_result[i].department)

    def test_repository(self) -> None:
        # Test repository functionalities
        file_path: str = "./support/instructors.txt"

        instructors: List[Instructor] = \
            Instructors.from_file(file_path)
        repository: Instructors = Instructors(instructors)

        self.assertEqual(len(repository.all()), 6)
        expected_instructor: Instructor = Instructor("98765",
                                                     "Einstein, A", "SFEN")

        teacher: Instructor = repository.get(instructor.GetBy.ID, "98765")
        self.assertEqual(expected_instructor.cwid, teacher.cwid)
        self.assertEqual(expected_instructor.name, teacher.name)
        self.assertEqual(expected_instructor.department,
                         teacher.department)
        self.assertEqual(len(
            repository.get(instructor.GetBy.DEPARTMENT, "SFEN")), 3)
        self.assertEqual(len(
            repository.get(instructor.GetBy.DEPARTMENT, "SYEN")), 3)
        with self.assertRaises(ValueError):
            repository.get(instructor.GetBy.ID, "TEST")


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
            Grades.from_file(file_path)

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

        grades: List[Grade] = Grades.from_file(file_path)
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
        expected: List[Tuple[str, str, List[str]]] = [
            ("10103", "Baldwin, C", ["CS 501", "SSW 564", "SSW 567",
                                     "SSW 687"]),
            ("10115", "Wyatt, X", ["CS 545", "SSW 564", "SSW 567", "SSW 687"]),
            ("10172", "Forbes, I", ["SSW 555", "SSW 567"])
        ]
        for i in range(len(summary[0:3])):
            self.assertEqual(summary[i], expected[i])
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


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
