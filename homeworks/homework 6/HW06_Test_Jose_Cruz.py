"""HW05: String methods, slices, working with files, and automated testing

    This class will test:
    - list_copy
    - list_intersect
    - list_difference

    CONVENTIONS:
    - Max character limit per line 80
    - CapWords for class names
    - snake_case for variables and functions
    - double quotes for strings

   Author: Jose J. Cruz
   CWID: 10467076
"""
import unittest
from typing import List

from HW06_Jose_Cruz import list_copy, list_intersect, list_difference


class ListCopyTest(unittest.TestCase):
    """Test suite for list_copy"""

    def test_type_error(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, list_copy, 0)
        self.assertRaises(TypeError, list_copy, "a")
        self.assertRaises(TypeError, list_copy, 11.1)

    def test_list_copy(self) -> None:
        """Test that all the values in the original list exist in the copy
        and are in the same order"""
        original_list: List[any] = [1, "b", True, 9.99]
        copied_list: List[any] = list_copy(original_list)
        self.assertEqual(original_list, copied_list)
        for index, item in enumerate(original_list):
            self.assertEqual(item, copied_list[index])

    def test_list_copy_not_same_reference(self) -> None:
        """Test that the copied array do not have the same identity as the
        original"""
        original_list: List[any] = [1, "b", True, 9.99]
        copied_list: List[any] = list_copy(original_list)
        self.assertNotEqual(id(original_list), id(copied_list))


class ListIntersectTest(unittest.TestCase):
    """Test suite for list_intersect"""

    def test_type_error(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, list_intersect, 0)
        self.assertRaises(TypeError, list_intersect, "a")
        self.assertRaises(TypeError, list_intersect, 11.1)
        self.assertRaises(TypeError, list_intersect, [])
        self.assertRaises(TypeError, list_intersect, [], "a")
        self.assertRaises(TypeError, list_intersect, [], True)
        self.assertRaises(TypeError, list_intersect, [], 9)

    def test_list_intersect(self) -> None:
        """Test that list_intersect"""
        self.assertEqual(list_intersect([1, 2, 3], [1, 4, 5]), [1])
        self.assertEqual(list_intersect([1, 2, 3], [1, 2, 4]), [1, 2])
        self.assertEqual(list_intersect([], []), [])
        self.assertEqual(list_intersect([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(list_intersect(list("abc"), list("axy")), ["a"])
        self.assertEqual(list_intersect([1, 2, 3, 1], [3, 4, 1, 5]), [1, 3])


class ListDifferenceTest(unittest.TestCase):
    """Test suite for list_difference"""

    def test_type_error(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, list_difference, 0)
        self.assertRaises(TypeError, list_difference, "a")
        self.assertRaises(TypeError, list_difference, 11.1)
        self.assertRaises(TypeError, list_difference, [])
        self.assertRaises(TypeError, list_difference, [], "a")
        self.assertRaises(TypeError, list_difference, [], True)
        self.assertRaises(TypeError, list_difference, [], 9)

    def test_list_intersect(self) -> None:
        """Test that list_intersect"""
        self.assertEqual(list_difference([1, 2, 3], [1, 4, 5]), [2, 3])
        self.assertEqual(list_difference([], []), [])
        self.assertEqual(list_difference([1, 2, 3], [1, 2, 4]), [3])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
