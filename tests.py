import unittest
from calculator import add, substract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,2), 5)
        self.assertEqual(add(-1,1), 0)


    def test_substract(self):
        self.assertEqual(add(3,2), 1)
        self.assertEqual(add(-1,1), -2)


    def test_multiple(self):
        self.assertEqual(multiply(3,2), 6)
        self.assertEqual(multiply(-1,1), -1)

    def test_divide(self):
        self.assertEqual(divide(6,2), 3)
        self.assertEqual(divide(3,2), 1.5)

        with self.assertRaises(ValueError):
            divide(4,0)


if __name__ == "__main__":
    unittest.main()