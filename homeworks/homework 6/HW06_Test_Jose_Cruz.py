"""HW05: String methods, slices, working with files, and automated testing

    This class will test:
    - list_copy
    - list_intersect
    - list_difference
    - remove_vowels

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

from HW06_Jose_Cruz import list_copy, list_intersect, list_difference, \
    remove_vowels, check_pwd, Costumer, DonutQueue, reorder


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

    def test_list_difference(self) -> None:
        """Test that list_difference"""
        self.assertEqual(list_difference([1, 2, 3], [1, 4, 5]), [2, 3])
        self.assertEqual(list_difference([], []), [])
        self.assertEqual(list_difference([1, 2, 3], [1, 2, 4]), [3])


class RemoveVowelsTest(unittest.TestCase):
    """Test suite for remove_vowels"""

    def test_type_error(self) -> None:
        """Tests that only string are pass as arguments"""
        self.assertRaises(TypeError, remove_vowels, 0)
        self.assertRaises(TypeError, remove_vowels, 9.99)
        self.assertRaises(TypeError, remove_vowels, True)

    def test_remove_vowels(self) -> None:
        """Test list_intersect"""
        self.assertEqual(remove_vowels("Amy is my favorite daughter"),
                         "my favorite daughter")
        self.assertEqual(remove_vowels("Jan is my best friend"),
                         "Jan my best friend")
        self.assertEqual(remove_vowels("Once upon a time"), "time")
        self.assertEqual(remove_vowels(""), "")
        # Overwatch reference
        self.assertEqual(remove_vowels("Heroes never die"), "Heroes never die")


class CheckPWDTest(unittest.TestCase):
    """Test suite for check_pwd"""

    def test_type_error(self) -> None:
        """Tests that only string are pass as arguments"""
        self.assertRaises(TypeError, check_pwd, 0)
        self.assertRaises(TypeError, check_pwd, 9.99)
        self.assertRaises(TypeError, check_pwd, True)

    def test_check_pwd(self) -> None:
        """Test check_pwd"""
        self.assertFalse(check_pwd(""))
        self.assertFalse(check_pwd("AAo"))
        self.assertFalse(check_pwd("A1Ao"))
        self.assertFalse(check_pwd('AAo1'))
        self.assertFalse(check_pwd('1Aao'))
        self.assertFalse(check_pwd('1AAO'))
        self.assertTrue("1AAo")
        self.assertTrue("1789May5")


class DonutQueueTest(unittest.TestCase):
    """Test Donut Queue"""

    def test_type_error(self) -> None:
        """Tests that only string and boolean are pass as arguments"""
        self.assertRaises(TypeError, Costumer, 0)
        self.assertRaises(ValueError, Costumer, "")
        self.assertRaises(TypeError, Costumer, "Lucas", 9)
        self.assertRaises(TypeError, Costumer, "John", "Dow")

    def test_queue(self) -> None:
        """Tests the donut queue"""
        queue: DonutQueue = DonutQueue()
        self.assertIsNone(queue.next_customer())
        queue.arrive("Sujit", False)
        queue.arrive("Fei", False)
        queue.arrive("Prof JR", True)
        self.assertEqual(queue.waiting(), "Prof JR, Sujit, Fei")
        queue.arrive("Nanda", True)
        self.assertEqual(queue.waiting(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(queue.next_customer(), "Prof JR")
        self.assertEqual(queue.next_customer(), "Nanda")
        self.assertEqual(queue.next_customer(), "Sujit")
        self.assertEqual(queue.waiting(), "Fei")
        self.assertEqual(queue.next_customer(), "Fei")
        self.assertIsNone(queue.next_customer())


class ReorderTest(unittest.TestCase):
    """Test suite for reorder"""

    def test_type_error(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, reorder, 0)
        self.assertRaises(TypeError, reorder, "a")
        self.assertRaises(TypeError, reorder, 11.1)

    def test_reorder(self) -> None:
        """Test reorder"""
        self.assertEqual(reorder([1, 5, 3, 3]), [1, 3, 3, 5])
        self.assertEqual(reorder([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(reorder([5, 5, 5, 1]), [1, 5, 5, 5])
        self.assertEqual(reorder([2, 2, 5, 1]), [1, 2, 2, 5])
        self.assertEqual(reorder(list('aiueo')), ['a', 'e', 'i', 'o', 'u'])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
