import unittest
from pywallet.product import Product

class TestProductValidationMethods(unittest.TestCase):
    
    def test_negative_value(self):
        with self.assertRaises(ValueError):
            Product.validateValue(-10)
            
    def test_invalid_constructor(self):
        with self.assertRaises(ValueError):
            Product("A", -10)