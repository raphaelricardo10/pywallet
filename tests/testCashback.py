import unittest
from cashback.cashback import *

class TestCashbackMethods(unittest.TestCase):
    
    def test_cashback_ok(self):
        result = calculateCashback(150, 5)
        self.assertEqual(result, 7.5)