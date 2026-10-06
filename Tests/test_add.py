import unittest
from fraction import Fraction

class TestFractionAddition(unittest.TestCase):

    def test_add_two_fractions(self):
        self.assertEqual(Fraction(5,6), Fraction(1,2) + Fraction(1,3))

    def test_add_fraction_and_integer(self):
        self.assertEqual(Fraction(3,2), Fraction(1,2) + 1)

    def test_add_normalizes_result(self):
        self.assertEqual(Fraction(1,2), Fraction(1,4) + Fraction(1,4))

    def test_add_does_not_modify_left_operand(self):
        left = Fraction(1, 2)
        left + Fraction(1, 3)
        self.assertEqual(Fraction(1, 2), left)

    def test_add_does_not_modify_right_operand(self):
        right = Fraction(1, 6)
        Fraction(1, 3) + right
        self.assertEqual(Fraction(1, 6), right)

    def test_add_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + "hello"

    def test_add_float_raises_type_error(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + .5

    def test_add_negative_fraction(self):
        self.assertEqual(Fraction(1, 6), Fraction(1, 2) + Fraction(-1, 3))