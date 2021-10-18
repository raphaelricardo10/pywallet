import unittest
from cashback import cashbackTypes

class TestCashback(unittest.TestCase):
    
    def test_cashback_ok(self):
        cashback = cashbackTypes.ConstantByTotal(5, 150)
        self.assertEqual(cashback.value, 7.5)

    def test_negative_percent(self):
        with self.assertRaises(ValueError):
            cashbackTypes.ConstantByTotal(-5, 150)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            cashbackTypes.ConstantByTotal(5, -150)

    def test_variable_percents(self):
        breakpoints = [
            # Total: 0 means the minimum cashback.
            # If it is not defined, the minimum cashback will be zero
            {
                'total': 0,
                'percent': 5
            },
            {
                'total': 500,
                'percent': 8
            },
            {
                'total': 1500,
                'percent': 10
            }
        ]

        cashback = cashbackTypes.VariableByTotal(breakpoints, 750)
        self.assertEqual(cashback.value, 60)