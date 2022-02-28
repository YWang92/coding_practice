import unittest
from last_digit_of_fibonacci_number import last_digit_of_fibonacci_number


class TestLastDigitOfFibonacciNumber(unittest.TestCase):


    def test_large(self):
        for (n, last_digit) in [(100, 5), (139, 1), (91239, 6), (10000, 5)]:
            self.assertEqual(last_digit_of_fibonacci_number(n), last_digit)


if __name__ == '__main__':
    unittest.main()
