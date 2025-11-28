import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---- ADDITION TESTS ----
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    # ---- SUBTRACTION TESTS ----
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    # ---- MULTIPLICATION TESTS ----
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(1.5, 1.5), 2.25)

    # ---- DIVISION TESTS ----
    def test_division(self):
        self.assertEqual(self.calc.divide(20, 5), 4.0)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(-9, -3), 3.0)
        self.assertAlmostEqual(self.calc.divide(10, 3), 10/3)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertEqual(self.calc.divide(5, 0), None)

    # ---- TYPE SAFETY / UNEXPECTED INPUTS ----
    def test_string_input(self):
        with self.assertRaises(TypeError):
            self.calc.add("2", 3)
        with self.assertRaises(TypeError):
            self.calc.subtract(5, "1")
        with self.assertRaises(TypeError):
            self.calc.multiply("a", "b")
        self.assertIsNone(self.calc.divide("10", 2))  # this will raise TypeError, ensuring robust test coverage

    def test_large_numbers(self):
        self.assertEqual(self.calc.add(10**10, 10**10), 2 * 10**10)
        self.assertEqual(self.calc.multiply(10**5, 10**5), 10**10)
        self.assertEqual(self.calc.subtract(10**10, 10**9), 9 * 10**9)

    def test_float_precision(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.2), 0.1)
        self.assertAlmostEqual(self.calc.multiply(0.1, 3), 0.3)

    def test_negative_division(self):
        self.assertEqual(self.calc.divide(-15, 3), -5.0)

if __name__ == "__main__":
    unittest.main()
