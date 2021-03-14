"""HW04: Sequence, Iterators and Generators

    This class will test:
    -

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

from HW05_Jose_Cruz import reverse, substring, find_second


class ReverseTest(unittest.TestCase):
    """Test suite for reverse words"""

    def test_type_error(self) -> None:
        """Test type error in count_vowels"""
        self.assertRaises(TypeError, reverse, 0)
        self.assertRaises(TypeError, reverse, ["a"])
        self.assertRaises(TypeError, reverse, 11.1)

    def test_reverse(self) -> None:
        """Test count vowels function"""
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
    """Test suite for substring function"""

    def test_type_error(self) -> None:
        """Test type error in substring"""
        self.assertRaises(TypeError, find_second, 0, 0)
        self.assertRaises(TypeError, find_second, ["a"], "a")
        self.assertRaises(TypeError, find_second, 11.1, 0)
        self.assertRaises(TypeError, find_second, "a", 1)
        self.assertRaises(TypeError, find_second, "a", 11.1)

    def test_find_second(self) -> None:
        """Test the substring function"""
        self.assertEqual(find_second("he", "hello"), -1)
        self.assertEqual(find_second("l", "hello"), 3)
        self.assertEqual(find_second("xxx", "hello"), -1)
        self.assertEqual(find_second("iss", "Mississippi"), 4)
        self.assertEqual(find_second("abba", "abbabba"), 3)
        self.assertEqual(find_second("ab", "abbabba"), 3)
        self.assertEqual(find_second("ba", "abbabba"), 5)
        self.assertEqual(find_second("a", "abbabba"), 3)
        self.assertEqual(find_second("ax", "abbaxbba"), -1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
