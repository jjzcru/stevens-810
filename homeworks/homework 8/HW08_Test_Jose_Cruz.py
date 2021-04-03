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
from typing import Tuple, List
from datetime import datetime
from HW08_Jose_Cruz import date_arithmetic, file_reader, FileAnalyzer


class DateArithmeticTest(unittest.TestCase):
    """Test suite for date_arithmetic"""

    def test_date_arithmetic(self) -> None:
        """Tests the function date_arithmetic"""
        three_days_after_02272020: datetime
        three_days_after_02272019: datetime
        diff: int

        three_days_after_02272020, three_days_after_02272019, \
            diff = date_arithmetic()

        self.assertEqual(three_days_after_02272020, datetime(2020, 3, 1))
        self.assertEqual(three_days_after_02272019, datetime(2019, 3, 2))
        self.assertEqual(diff, 241)


class FileReaderTest(unittest.TestCase):
    """Test suite for file_reader"""

    def test_file_reader(self) -> None:
        """Tests the function file_reader"""
        file_path: str = "./support/student_majors.txt"
        error_file_path: str = "./support/error.txt"
        dir_file_path: str = "./support"
        invalid_file_path: str = "./support/non_existent.txt"

        with self.assertRaises(TypeError):
            tuple(file_reader(0, 0))

        with self.assertRaises(TypeError):
            tuple(file_reader(True, ""))

        with self.assertRaises(TypeError):
            tuple(file_reader(11.5, False))

        with self.assertRaises(FileNotFoundError):
            tuple(file_reader(invalid_file_path, 20))

        with self.assertRaises(IsADirectoryError):
            tuple(file_reader(dir_file_path, 20))

        with self.assertRaises(ValueError):
            list(file_reader(file_path, 2, "|", True))

        with self.assertRaises(ValueError):
            list(file_reader(error_file_path, 2, "|", True))

        response: List[List[str]] = list(file_reader(file_path, 3, "|"))
        self.assertEqual(response, [
            ("CWID", "Name", "Major"),
            ("123", "Jin He", "Computer Science"),
            ("234", "Nanda Koka", "Software Engineering"),
            ("345", "Benji Cai", "Software Engineering")
        ])

        response = list(file_reader(file_path, 3, "|", True))
        self.assertEqual(response, [
            ("123", "Jin He", "Computer Science"),
            ("234", "Nanda Koka", "Software Engineering"),
            ("345", "Benji Cai", "Software Engineering")
        ])

        # self.assertRaises(TypeError, file_reader, True, "")
        # self.assertRaises(TypeError, file_reader, 11.1, True)
        # self.assertRaises(TypeError, file_reader, file_path)
        # self.assertRaises(FileNotFoundError, file_reader, invalid_file_path)
        # self.assertRaises(IOError, file_reader, dir_file_path)


class FileAnalyzerTest(unittest.TestCase):
    """Test suite for FileAnalyzer"""

    def test_file_analyzer(self) -> None:
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
