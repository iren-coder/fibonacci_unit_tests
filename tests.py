from fibonacci import find_fibonacci
from unittest import TestCase


class FibonacciTestCase(TestCase):
    def test_first_fibonacci_number_is_1(self):
        x = find_fibonacci(1)
        self.assertEqual(1, x)

    def test_second_fibonacci_number_is_1(self):
        x = find_fibonacci(2)
        self.assertEqual(1, x)

    def test_5th_fibonacci_number_is_5(self):
        x = find_fibonacci(5)
        self.assertEqual(5, x)