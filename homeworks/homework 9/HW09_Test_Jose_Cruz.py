"""HW05: String methods, slices, working with files, and automated testing

    This class will test:
    - date_arithmetic
    - file_reader
    - anagrams_cntr
    - covers_alphabet
    - web_analyzer

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
from datetime import datetime
from HW09_Jose_Cruz import StudentRepository, Student


class StudentRepositoryTest(unittest.TestCase):
    """Test suite for StudentRepository"""

    def test_from_file(self) -> None:
        # Test getting a list of student from file
        non_existing_file_path: str = "./test"
        dir_path: str = "./support"
        file_path: str = "./support/students.txt"

        with self.assertRaises(TypeError):
            StudentRepository.from_file(0)

        with self.assertRaises(FileNotFoundError):
            StudentRepository.from_file(non_existing_file_path)

        with self.assertRaises(ValueError):
            StudentRepository.from_file(dir_path)

        students: List[Student] = StudentRepository.from_file(file_path)

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

        students: List[Student] = StudentRepository.from_file(file_path)
        repository: StudentRepository = StudentRepository(students)

        self.assertEqual(len(repository.students), 10)
        expected_student: Student = Student("10103", "Baldwin, C", "SFEN")
        student: Student = repository.find_by_id("10103")
        self.assertEqual(expected_student.cwid, student.cwid)
        self.assertEqual(expected_student.name, student.name)
        self.assertEqual(expected_student.major, student.major)

        self.assertEqual(len(repository.find_by_major("SFEN")), 5)
        self.assertEqual(len(repository.find_by_major("SYEN")), 5)
        self.assertIsNone(repository.find_by_id("TEST"))
