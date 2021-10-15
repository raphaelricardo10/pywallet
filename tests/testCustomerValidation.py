import unittest
from pywallet.customer import Customer

class TestCustomerValidationMethods(unittest.TestCase):

    def test_cpf_validation(self):
        with self.assertRaises(Customer.InvalidCpfError):
            Customer.validateCpf("12312312365")

    def test_constructor_validation(self):
        with self.assertRaises(Customer.InvalidCpfError):
            Customer("Raphael Ricardo", "12312312365")