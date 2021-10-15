import unittest

class TestCashbackMethods(unittest.TestCase):
    
    def test_cashback_ok(self):
        result = calculateCashback(100, 5)
        self.assertEqual(result, 5)