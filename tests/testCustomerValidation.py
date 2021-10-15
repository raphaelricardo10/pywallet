import unittest
from pywallet.customer import Customer

class TestCustomerValidationMethods(unittest.TestCase):

    def test_cpf_validation(self):
        with self.assertRaises(ValueError):
            Customer.validateCpf("12312312365")