import unittest
from yaml import load
from json import dumps
from cashback.orderHTTP import OrderHTTP

# Create your tests here.
class TestOrderHTTP(unittest.TestCase):

    def test_create_order_ok(self):
        with open('tests/inputs/salesRightInputs.yaml') as json:
            for obj in load(json):
                order = OrderHTTP(dumps(obj['input']), 5)
                output = obj['output']
                self.assertEqual(order.customer.name, output['name'])
                self.assertEqual(order.customer.document, output['document'])
                self.assertEqual(order.total, output['total'])

    def test_wrong_inputs(self):
        with open('tests/inputs/salesWrongInputs.yaml') as json:
            with self.assertRaises(Exception):
                for obj in load(json):
                    order = OrderHTTP(dumps(obj['input']))