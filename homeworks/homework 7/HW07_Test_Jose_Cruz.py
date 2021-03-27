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

from HW07_Jose_Cruz import anagrams_lst, anagrams_dd, anagrams_cntr


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

    def test_anagrams_dd(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, anagrams_dd, 0)
        self.assertRaises(TypeError, anagrams_dd, 0, 20)
        self.assertRaises(TypeError, anagrams_dd, True)
        self.assertRaises(TypeError, anagrams_dd, True, '')
        self.assertRaises(TypeError, anagrams_dd, 11.1)
        self.assertRaises(TypeError, anagrams_dd, 11.1, [])
        self.assertRaises(ValueError, anagrams_dd, '', '')
        self.assertRaises(ValueError, anagrams_dd, '', '111')
        self.assertRaises(ValueError, anagrams_dd, '111', '')
        self.assertTrue(anagrams_dd('hello', 'olleh'))
        self.assertTrue(anagrams_dd('hello', 'holle'))
        self.assertTrue(anagrams_dd('dusty', 'study'))
        self.assertTrue(anagrams_dd('night', 'thing'))
        self.assertTrue(anagrams_dd('Inch', 'Chin'))
        self.assertTrue(anagrams_dd('Night', 'Thing'))
        self.assertFalse(anagrams_lst('hello', 'ollehh'))
        self.assertFalse(anagrams_lst('hello', 'ollehh'))

    def test_anagrams_cntr(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, anagrams_cntr, 0)
        self.assertRaises(TypeError, anagrams_cntr, 0, 20)
        self.assertRaises(TypeError, anagrams_cntr, True)
        self.assertRaises(TypeError, anagrams_cntr, True, '')
        self.assertRaises(TypeError, anagrams_cntr, 11.1)
        self.assertRaises(TypeError, anagrams_cntr, 11.1, [])
        self.assertRaises(ValueError, anagrams_cntr, '', '')
        self.assertRaises(ValueError, anagrams_cntr, '', '111')
        self.assertRaises(ValueError, anagrams_cntr, '111', '')
        self.assertTrue(anagrams_cntr('hello', 'olleh'))
        self.assertTrue(anagrams_cntr('hello', 'holle'))
        self.assertTrue(anagrams_cntr('dusty', 'study'))
        self.assertTrue(anagrams_cntr('night', 'thing'))
        self.assertFalse(anagrams_cntr('hello', 'ollehh'))
        self.assertFalse(anagrams_cntr('hello', 'ollehh'))
