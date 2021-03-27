"""HW05: String methods, slices, working with files, and automated testing

    This class will test:
    - anagrams_lst
    - anagrams_dd
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
from typing import Dict, List, Tuple
from HW07_Jose_Cruz import anagrams_lst, anagrams_dd, anagrams_cntr, \
    covers_alphabet, web_analyzer


class AnagramTest(unittest.TestCase):
    """Test suite for anagrams"""

    def test_anagrams_lst(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, anagrams_lst, 0)
        self.assertRaises(TypeError, anagrams_lst, 0, 20)
        self.assertRaises(TypeError, anagrams_lst, True)
        self.assertRaises(TypeError, anagrams_lst, True, "")
        self.assertRaises(TypeError, anagrams_lst, 11.1)
        self.assertRaises(TypeError, anagrams_lst, 11.1, [])
        self.assertRaises(ValueError, anagrams_lst, "", "")
        self.assertRaises(ValueError, anagrams_lst, "", "111")
        self.assertRaises(ValueError, anagrams_lst, "111", "")
        self.assertRaises(ValueError, anagrams_lst, "111", "111")
        self.assertTrue(anagrams_lst("hello", "olleh"))
        self.assertTrue(anagrams_lst("hello", "holle"))
        self.assertTrue(anagrams_lst("dusty", "study"))
        self.assertTrue(anagrams_lst("night", "thing"))
        self.assertTrue(anagrams_lst("Adelina Yarelin", "Daniela Aerilyn"))
        self.assertFalse(anagrams_lst("hello", "ollehh"))
        self.assertFalse(anagrams_lst("hello", "ollehh"))

    def test_anagrams_dd(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, anagrams_dd, 0)
        self.assertRaises(TypeError, anagrams_dd, 0, 20)
        self.assertRaises(TypeError, anagrams_dd, True)
        self.assertRaises(TypeError, anagrams_dd, True, "")
        self.assertRaises(TypeError, anagrams_dd, 11.1)
        self.assertRaises(TypeError, anagrams_dd, 11.1, [])
        self.assertRaises(ValueError, anagrams_dd, "", "")
        self.assertRaises(ValueError, anagrams_dd, "", "111")
        self.assertRaises(ValueError, anagrams_dd, "111", "")
        self.assertRaises(ValueError, anagrams_lst, "aaaa", "a1aaa")
        self.assertTrue(anagrams_dd("hello", "olleh"))
        self.assertTrue(anagrams_dd("hello", "holle"))
        self.assertTrue(anagrams_dd("dusty", "study"))
        self.assertTrue(anagrams_dd("night", "thing"))
        self.assertTrue(anagrams_dd("Inch", "Chin"))
        self.assertTrue(anagrams_dd("Adelina Yarelin", "Daniela Aerilyn"))
        self.assertTrue(anagrams_dd("Night", "Thing"))
        self.assertFalse(anagrams_lst("hello", "ollehh"))
        self.assertFalse(anagrams_lst("hello", "ollehh"))

    def test_anagrams_cntr(self) -> None:
        """Tests that only list are pass as arguments"""
        self.assertRaises(TypeError, anagrams_cntr, 0)
        self.assertRaises(TypeError, anagrams_cntr, 0, 20)
        self.assertRaises(TypeError, anagrams_cntr, True)
        self.assertRaises(TypeError, anagrams_cntr, True, "")
        self.assertRaises(TypeError, anagrams_cntr, 11.1)
        self.assertRaises(TypeError, anagrams_cntr, 11.1, [])
        self.assertRaises(ValueError, anagrams_cntr, "", "")
        self.assertRaises(ValueError, anagrams_cntr, "", "111")
        self.assertRaises(ValueError, anagrams_cntr, "111", "")
        self.assertRaises(ValueError, anagrams_lst, "aaaa", "a1aaa")
        self.assertTrue(anagrams_cntr("hello", "olleh"))
        self.assertTrue(anagrams_cntr("hello", "holle"))
        self.assertTrue(anagrams_cntr("dusty", "study"))
        self.assertTrue(anagrams_cntr("Adelina Yarelin", "Daniela Aerilyn"))
        self.assertTrue(anagrams_cntr("night", "thing"))
        self.assertFalse(anagrams_cntr("hello", "ollehh"))
        self.assertFalse(anagrams_cntr("hello", "ollehh"))


class CoversAlphabetTest(unittest.TestCase):
    """Test suite for covers alphabet"""

    def test_covers_alphabet(self) -> None:
        """Tests covers_alphabet function"""
        self.assertRaises(TypeError, covers_alphabet, 0)
        self.assertRaises(TypeError, covers_alphabet, True)
        self.assertRaises(TypeError, covers_alphabet, 11.1)
        self.assertRaises(TypeError, covers_alphabet, [])
        self.assertTrue(covers_alphabet("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"))
        self.assertTrue(covers_alphabet("The quick brown fox jumps over the "
                                        "lazy dog"))
        self.assertTrue(covers_alphabet("We promptly judged antique ivory "
                                        "buckles for the next prize"))
        self.assertFalse(covers_alphabet("abcdefghijklmnopqrstuvwxy"))
        self.assertFalse(covers_alphabet("bcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(covers_alphabet(""))
        self.assertFalse(covers_alphabet("xyz"))
        self.assertTrue(covers_alphabet("The quick, brown, fox; jumps over "
                                        "the lazy dog!"))


class WebAnalyzerTest(unittest.TestCase):
    """Test suite for Web analyzer"""

    def test_web_analyzer(self) -> None:
        """Tests that only list are pass as arguments"""
        weblogs: List[Tuple[str, str]] = [
            ("Nanda", "google.com"),
            ("Maha", "google.com"),
            ("Fei", "python.org"),
            ("Maha", "google.com"),
            ("Fei", "python.org"),
            ("Nanda", "python.org"),
            ("Fei", "dzone.com"),
            ("Nanda", "google.com"),
            ("Maha", "google.com"), ]

        summary: List[Tuple[str, List[str]]] = [
            ("dzone.com", ["Fei"]),
            ("google.com", ["Maha", "Nanda"]),
            ("python.org", ["Fei", "Nanda"]), ]

        self.assertRaises(TypeError, web_analyzer, 0)

        self.assertRaises(TypeError, web_analyzer, True)
        self.assertRaises(TypeError, web_analyzer, 11.1)
        self.assertRaises(TypeError, web_analyzer, ["google.com"])
        self.assertRaises(TypeError, web_analyzer, [True])
        self.assertRaises(TypeError, web_analyzer, [["example"]])
        self.assertRaises(ValueError, web_analyzer, [("example", 3)])
        self.assertRaises(ValueError, web_analyzer, [("example", True)])
        self.assertRaises(ValueError, web_analyzer, [("example", "example",
                                                      "example")])
        self.assertRaises(ValueError, web_analyzer, [(True, "Test")])
        self.assertEqual(web_analyzer([]), [])
        self.assertEqual(web_analyzer(weblogs), summary)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
