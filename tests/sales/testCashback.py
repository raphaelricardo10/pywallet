import unittest
from cashback import cashbackTypes

class TestCashback(unittest.TestCase):
    
    def test_cashback_ok(self):
        cashback = cashbackTypes.ConstantByTotal(150, 5)
        self.assertEqual(cashback.value, 7.5)

    def test_negative_percent(self):
        with self.assertRaises(ValueError):
            cashbackTypes.ConstantByTotal(150, -5)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            cashbackTypes.ConstantByTotal(-150, 5)