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

from HW07_Jose_Cruz import anagrams_lst


class AnagramTest(unittest.TestCase):
    """Test suite for anagrams"""

    def test_anagrams_lst(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, anagrams_lst, 0)
        self.assertRaises(TypeError, anagrams_lst, 0, 20)
        self.assertRaises(TypeError, anagrams_lst, True)
        self.assertRaises(TypeError, anagrams_lst, True, '')
        self.assertRaises(TypeError, anagrams_lst, 11.1)
        self.assertRaises(TypeError, anagrams_lst, 11.1, [])
        self.assertRaises(ValueError, anagrams_lst, '', '')
        self.assertRaises(ValueError, anagrams_lst, '', '111')
        self.assertRaises(ValueError, anagrams_lst, '111', '')
        self.assertTrue(anagrams_lst('hello', 'olleh'))
        self.assertTrue(anagrams_lst('hello', 'holle'))
        self.assertTrue(anagrams_lst('dusty', 'study'))
        self.assertTrue(anagrams_lst('night', 'thing'))
        self.assertFalse(anagrams_lst('hello', 'ollehh'))
        self.assertFalse(anagrams_lst('hello', 'ollehh'))
