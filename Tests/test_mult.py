import unittest

from fraction import Fraction


class TestFractionMultiplication(unittest.TestCase):
  def test_multiplies_two_fractions_and_normalizes_result(self):
    product = Fraction(2, 3).__mul__(Fraction(9, 10))

    self.assertEqual(Fraction(3, 5), product)

  def test_multiplies_fraction_by_integer(self):
    product = Fraction(3, 4).__mul__(2)

    self.assertEqual(Fraction(3, 2), product)

  def test_does_not_modify_operands(self):
    fraction = Fraction(2, 3)
    other = Fraction(9, 10)

    fraction.__mul__(other)

    self.assertEqual(Fraction(2, 3), fraction)
    self.assertEqual(Fraction(9, 10), other)

  def test_raises_type_error_for_unsupported_operand(self):
    with self.assertRaises(TypeError):
      Fraction(1, 2).__mul__(0.5)


if __name__ == "__main__":
  unittest.main()
