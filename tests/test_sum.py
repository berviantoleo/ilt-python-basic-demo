# test_sum.py
import unittest

import operation.sum as operation_sum

class TestSum(unittest.TestCase):
    def test_sum_zero(self):
        # Assert that the function output equals the expected result
        self.assertEqual(operation_sum.sum(0, 0), 0)

    def test_sum_positive_numbers(self):
        self.assertEqual(operation_sum.sum(2, 3), 5)

    def test_sum_negative_numbers(self):
        self.assertEqual(operation_sum.sum(-2, -3), -5)

    def test_sum_mixed_numbers(self):
        self.assertEqual(operation_sum.sum(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()
