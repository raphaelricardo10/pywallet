import unittest
from pywallet.product import Product
from pywallet.order import Order

class TestOrderValidationMethods(unittest.TestCase):
    
    def test_total_order_ok(self):
        order = Order()
        order.addItem(Product("A", 10), 2)
        order.addItem(Product("B", 30), 3)
        
        self.assertEqual(order.total, 110)