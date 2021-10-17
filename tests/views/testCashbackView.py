import unittest
from yaml import load
from json import dumps
from cashback.orderHTTP import orderHTTP

# Create your tests here.
class TestOrderHTTP(unittest.TestCase):

    def test_create_order_ok(self):
        with open('cashback/testInputs/rightInputs.yaml') as json:
            for obj in load(json):
                order = orderHTTP(dumps(obj['input']))
                output = obj['output']
                self.assertEqual(order.customer.name, output['name'])
                self.assertEqual(order.customer.document, output['document'])
                self.assertEqual(order.total, output['total'])