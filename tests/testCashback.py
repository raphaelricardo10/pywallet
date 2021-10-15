import unittest
from cashback.cashback import *

class TestCashbackMethods(unittest.TestCase):
    
    def test_cashback_ok(self):
        result = calculateCashback(150, 5)
        self.assertEqual(result, 7.5)

    def test_negative_percent(self):
        with self.assertRaises(ValueError):
            calculateCashback(150, -5)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            calculateCashback(-150, 5)