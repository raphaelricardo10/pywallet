import unittest
from pywallet.customer import Customer

class TestCustomerValidationMethods(unittest.TestCase):

    def test_document_validation(self):
        with self.assertRaises(Customer.InvalidDocumentError):
            Customer.validateDocument("12312312365")

    def test_constructor_validation(self):
        with self.assertRaises(Customer.InvalidDocumentError):
            Customer("Raphael Ricardo", "12312312365")