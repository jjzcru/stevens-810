"""HW03: Fractions Unit Tests

   This class will test all the magic operators for the class Fraction

   CONVENTIONS:
   - Max character limit per line 80
   - CapWords for class names
   - snake_case for variables and functions
   - asertEqual for arithmetics operators
   - assertTrue for logical operators
   - assertRaises for test zero division

   Author: Jose J. Cruz
   CWID: 10467076
"""
import unittest
from HW03_Jose_Cruz import Fraction, gcf


class FractionTest(unittest.TestCase):
    """Test suite for Fractions functions"""
    def test_add(self) -> None:
        """Test the add operator"""
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), 1)
        self.assertEqual(Fraction(1, 3) + Fraction(1, 3), Fraction(2, 3))
        self.assertEqual(Fraction(200, 20) + Fraction(300, 30), 20)
        self.assertEqual(Fraction(1, 2) + Fraction(3, 4), Fraction(5, 4))
        self.assertEqual(Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3), 1)
        self.assertEqual(Fraction(1, 4) + Fraction(3, 4), 1)
        self.assertEqual(Fraction(4, 4) + Fraction(1, 2), Fraction(3, 2))

    def test_sub(self) -> None:
        """Test the subtract operator"""
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), 0)
        self.assertEqual(Fraction(1, 2) - Fraction(3, 4), Fraction(-1, 4))
        self.assertEqual(Fraction(5, 4) - Fraction(2, 4) - Fraction(1, 4),
                         Fraction(2, 4))
        self.assertEqual(Fraction(1, 4) - Fraction(3, 4), Fraction(-1, 2))
        self.assertEqual(Fraction(1, 2) - Fraction(4, 4), Fraction(-1, 2))

    def test_mul(self) -> None:
        """Test the multiply operator"""
        self.assertEqual(Fraction(1, 2) * Fraction(3, 4), Fraction(3, 8))
        self.assertEqual(Fraction(1, 3) * Fraction(1, 3) * Fraction(1, 3),
                         Fraction(1, 27))
        self.assertEqual(Fraction(1, 4) * Fraction(3, 4), Fraction(3, 16))
        self.assertEqual(Fraction(1, 2) * Fraction(4, 4), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2) * Fraction(1, 2), Fraction(1, 4))
        self.assertEqual(Fraction(4, 4) * Fraction(1, 2), Fraction(1, 2))

    def test_truediv(self) -> None:
        """Test the division operator"""
        self.assertEqual(Fraction(1, 2) / Fraction(3, 4), Fraction(2, 3))
        self.assertEqual(Fraction(1, 4) / Fraction(3, 4), Fraction(1, 3))
        self.assertEqual(Fraction(1, 2) / Fraction(4, 4), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2) / Fraction(1, 2), 1)
        self.assertEqual(Fraction(4, 4) / Fraction(1, 2), 2)
        self.assertEqual(Fraction(12, 8) / Fraction(4, 4), Fraction(3, 2))
        self.assertEqual(Fraction(12, 8) / Fraction(3, 2), 1)

    def test_equal(self) -> None:
        """Test equal operator"""
        self.assertTrue(Fraction(1, 2) == Fraction(1, 2))
        self.assertTrue(Fraction(1, 1) == Fraction(3, 3))
        self.assertTrue(Fraction(2, 4) == Fraction(1, 2))
        self.assertTrue(Fraction(1, 1) == Fraction(4, 4))
        self.assertTrue(Fraction(1, 2) == Fraction(1, 2))
        self.assertTrue(Fraction(1, 1) == 1)
        self.assertTrue(Fraction(2, 1) == 2)

    def test_not_equal(self) -> None:
        """Test not equal operator"""
        self.assertTrue(Fraction(1, 2) != Fraction(1, 3))
        self.assertTrue(Fraction(2, 2) != Fraction(3, 4))
        self.assertTrue(Fraction(3, 1) != Fraction(1, 2))
        self.assertTrue(Fraction(1, 3) != 1)
        self.assertTrue(Fraction(1, 2) != Fraction(1, 4))
        self.assertTrue(Fraction(1, 1) != 3)
        self.assertTrue(Fraction(2, 1) != 5)

    def test_less_than(self) -> None:
        """Test less than operator"""
        self.assertTrue(Fraction(1, 2) < Fraction(4, 2))
        self.assertTrue(Fraction(1, 1) < Fraction(4, 2))
        self.assertTrue(Fraction(5, 3) < Fraction(5, 2))

    def test_less_than_or_equal(self) -> None:
        """Test less than or equal operator"""
        self.assertTrue(Fraction(1, 2) <= Fraction(4, 2))
        self.assertTrue(Fraction(0, 1) <= Fraction(1, 1))
        self.assertTrue(Fraction(2, 3) <= Fraction(6, 9))

    def test_greater_than(self) -> None:
        """Test greater than operator"""
        self.assertTrue(Fraction(4, 2) > Fraction(1, 2))
        self.assertTrue(Fraction(4, 1) > Fraction(3, 1))
        self.assertTrue(Fraction(5, 3) > Fraction(4, 4))

    def test_greater_than_or_equal(self) -> None:
        """Test greater than or equal operator"""
        self.assertTrue(Fraction(4, 2) >= Fraction(8, 4))
        self.assertTrue(Fraction(4, 1) >= Fraction(3, 1))
        self.assertTrue(Fraction(5, 3) >= Fraction(5, 3))

    def test_str(self) -> None:
        """Test str method"""
        self.assertTrue(str(Fraction(1, 4)) == '1/4')
        self.assertTrue(str(Fraction(3, 4)) == '3/4')
        self.assertTrue(str(Fraction(2, 4)) == '2/4')

    def test_zero_denominator_error(self) -> None:
        """Test zero denominator exception"""
        self.assertRaises(ValueError, Fraction, 1, 0)
        self.assertRaises(ValueError, Fraction, 0, 0)
        self.assertRaises(ValueError, Fraction, 2, 0)

    def test_simplify(self) -> None:
        """Test simplify method for fractions"""
        self.assertEqual(str(Fraction(9, 27).simplify()), str(Fraction(1, 3)))
        self.assertEqual(str(Fraction(5, 10).simplify()), str(Fraction(1, 2)))
        self.assertEqual(str(Fraction(14, 7).simplify()), str(Fraction(2, 1)))
        self.assertEqual(str(Fraction(49, 7).simplify()), str(Fraction(7, 1)))
        self.assertEqual(str(Fraction(-49, 7).simplify()), str(Fraction(-7, 1)))


class GCFTest(unittest.TestCase):
    """Test suite for getting the greatest common factor"""

    def test_gcf(self) -> None:
        """Test getting the greatest common factor"""
        self.assertEqual(gcf(2, 4), 2)
        self.assertEqual(gcf(3, 6), 3)
        self.assertEqual(gcf(9, 3), 3)
        self.assertEqual(gcf(2, 5), 1)
        self.assertEqual(gcf(7, 13), 1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
