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
    """Test suite for anagrams"""

    def test_anagrams_lst(self) -> None:
        self.assertTrue(True)


class FileAnalyzerTest(unittest.TestCase):
    """Test suite for anagrams"""

    def test_anagrams_lst(self) -> None:
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
