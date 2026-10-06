import unittest

from fraction import Fraction


class TestFractionMultiplication(unittest.TestCase):
  def test_multiplies_two_fractions_and_normalizes_result(self):
    product = Fraction(2, 3).__mul__(Fraction(9, 10))

    self.assertEqual(Fraction(3, 5), product)

  def test_multiplies_fraction_by_integer(self):
    product = Fraction(3, 4).__mul__(2)

    self.assertEqual(Fraction(3, 2), product)

  def test_does_not_modify_left_operand(self):
    left = Fraction(2, 3)
    left.__mul__(Fraction(9, 10))

    self.assertEqual(Fraction(2, 3), left)

  def test_does_not_modify_right_operand(self):
    right = Fraction(9, 10)
    Fraction(2, 3).__mul__(right)

    self.assertEqual(Fraction(9, 10), right)

  def test_raises_type_error_for_unsupported_operand(self):
    with self.assertRaises(TypeError):
      Fraction(1, 2).__mul__(0.5)
      
  def test_multiplies_negative_fraction(self):
    product = Fraction(1, 2).__mul__(Fraction(-2, 3))

    self.assertEqual(Fraction(-1, 3), product)

if __name__ == "__main__":
  unittest.main()
