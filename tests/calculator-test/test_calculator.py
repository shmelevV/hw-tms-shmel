import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 2), 4)

    def test_subt(self):
        self.assertEqual(self.calculator.add(6, 2), 4)

    def test_mult(self):
        self.assertEqual(self.calculator.mult(2, 2), 4)

    def div(self):
        self.assertEqual(self.calculator.div(20, 10), 2)

    if __name__ == "__main__":
        unittest.main()
