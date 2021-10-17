import unittest
from sales import Cashback

class TestCashbackMethods(unittest.TestCase):
    
    def test_cashback_ok(self):
        cashback = Cashback(150, 5)
        self.assertEqual(cashback.value, 7.5)

    def test_negative_percent(self):
        with self.assertRaises(ValueError):
            Cashback(150, -5)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            Cashback(-150, 5)