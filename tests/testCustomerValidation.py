import unittest

class TestCustomerValidationMethods(unittest.TestCase):

    def test_cpf_validation(self):
        res = validateCPF(16149113710)
        self.assertTrue(res)