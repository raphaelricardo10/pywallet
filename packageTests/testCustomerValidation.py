import unittest
from sales import Customer

class TestCustomerValidationMethods(unittest.TestCase):

    def test_invalid_document(self):
        with self.assertRaises(Customer.InvalidDocumentError):
            Customer.validateDocument("12312312365")

    def test_invalid_constructor(self):
        with self.assertRaises(Customer.InvalidDocumentError):
            Customer("Raphael Ricardo", "12312312365")