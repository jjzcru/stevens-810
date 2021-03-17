"""HW05: String methods, slices, working with files, and automated testing

    This class will test:
    - reverse
    - substring
    - find_second
    - get_lines

    CONVENTIONS:
    - Max character limit per line 80
    - CapWords for class names
    - snake_case for variables and functions
    - asertEqual for arithmetics operators
    - assertTrue for logical operators
    - assertRaises for test zero division
    - assertLessEqual for attempts validation

   Author: Jose J. Cruz
   CWID: 10467076
"""
import unittest
from typing import List

from HW05_Jose_Cruz import reverse, substring, find_second, get_lines


class ReverseTest(unittest.TestCase):
    """Test suite for reverse words"""

    def test_type_error(self) -> None:
        """Test type error in reverse"""
        self.assertRaises(TypeError, reverse, 0)
        self.assertRaises(TypeError, reverse, ["a"])
        self.assertRaises(TypeError, reverse, 11.1)

    def test_reverse(self) -> None:
        """Test count reverse function"""
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("hhh"), "hhh")
        self.assertEqual(reverse("world"), "dlrow")
        self.assertEqual(reverse("w"), "w")


class SubstringTest(unittest.TestCase):
    """Test suite for substring function"""

    def test_type_error(self) -> None:
        """Test type error in substring"""
        self.assertRaises(TypeError, substring, 0, 0)
        self.assertRaises(TypeError, substring, ["a"], "a")
        self.assertRaises(TypeError, substring, 11.1, 0)
        self.assertRaises(TypeError, substring, "a", 1)
        self.assertRaises(TypeError, substring, "a", 11.1)

    def test_substring(self) -> None:
        """Test the substring function"""
        self.assertEqual(substring("he", "hello"), 0)
        self.assertEqual(substring("ell", "hello"), 1)
        self.assertEqual(substring("xxx", "hello"), -1)
        self.assertEqual(substring("o", "hello"), 4)


class FindSecondTest(unittest.TestCase):
    """Test suite for find_second function"""

    def test_type_error(self) -> None:
        """Test type error in find_second"""
        self.assertRaises(TypeError, find_second, 0, 0)
        self.assertRaises(TypeError, find_second, ["a"], "a")
        self.assertRaises(TypeError, find_second, 11.1, 0)
        self.assertRaises(TypeError, find_second, "a", 1)
        self.assertRaises(TypeError, find_second, "a", 11.1)

    def test_find_second(self) -> None:
        """Test the find_second function"""
        self.assertEqual(find_second("he", "hello"), -1)
        self.assertEqual(find_second("l", "hello"), 3)
        self.assertEqual(find_second("xxx", "hello"), -1)
        self.assertEqual(find_second("iss", "Mississippi"), 4)
        self.assertEqual(find_second("abba", "abbabba"), 3)
        self.assertEqual(find_second("ab", "abbabba"), 3)
        self.assertEqual(find_second("ba", "abbabba"), 5)
        self.assertEqual(find_second("a", "abbabba"), 3)
        self.assertEqual(find_second("ax", "abbaxbba"), -1)


class GetLinesTest(unittest.TestCase):
    """Test suite for get_lines function"""

    def test_type_error(self) -> None:
        """Test type error in get_lines"""
        with self.assertRaises(TypeError):
            list(get_lines(True))
        with self.assertRaises(TypeError):
            list(get_lines(0))
        with self.assertRaises(TypeError):
            list(get_lines(0.9))

    def test_file_not_found_error(self) -> None:
        """Test get_lines for files that do not exist"""
        with self.assertRaises(FileNotFoundError):
            test_file_path = 'HW05.test'
            list(get_lines(test_file_path))

    def test_file_path_is_dir(self) -> None:
        """Test get_lines for file path that are directories"""
        with self.assertRaises(IOError):
            test_file_path = 'support/HW05_DIR'
            list(get_lines(test_file_path))

    def test_get_lines(self) -> None:
        """Test the get_lines function"""
        test_file_path = 'support/HW05.txt'

        expect: List[str] = [
            '<line0>',
            '<line1>',
            '<line2>',
            '<line3.1 line3.2 line3.3>',
            '<line4.1 line4.2>',
            '<line5>',
            '<line6>'
        ]
        result: List[str] = list(get_lines(test_file_path))
        self.assertEqual(result, expect)

    def test_get_lines_with_empty_lines(self) -> None:
        """Test the get_lines function for document with empty lines"""
        test_file_path = 'support/HW05_2.txt'

        expect: List[str] = [
            '<line0>',
            '<line1>',
            '<line2>',
            '<line3.1 line3.2 line3.3>',
            '<line4.1 line4.2>',
            '<line5>',
            '',
            '<line6>'
        ]
        result: List[str] = list(get_lines(test_file_path))
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
