import unittest
from cashback.orderHTTP import orderHTTP

# Create your tests here.
class TestCashbackView(unittest.TestCase):

    def test_order_http(self):
        json = '{ "sold_at": "2026-01-02 00:00:00", "customer": { "document": "16149113710", "name": "JOSE DA SILVA" }, "total": "100.00", "products": [{ "type": "A", "value": "10.00", "qty": 1 }, { "type": "B", "value": "10.00", "qty": 9 }] }'
        order = orderHTTP(json)
        self.assertEqual(order.customer.name, 'JOSE DA SILVA')
        self.assertEqual(order.customer.document, '16149113710')
        self.assertEqual(order.total, 100)