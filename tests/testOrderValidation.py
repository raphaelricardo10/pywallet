import unittest
from datetime import datetime
from pywallet.product import Product
from pywallet.order import Order
from pywallet.customer import Customer

class TestOrderValidationMethods(unittest.TestCase):
    
    def test_total_order_ok(self):
        order = Order()
        order.addItem(Product("A", 10), 2)
        order.addItem(Product("B", 30), 3)
        
        self.assertEqual(order.total, 110)

    def test_reassign_total(self):
        order = Order()
        with self.assertRaises(AttributeError):
            order.total = 150

    def test_constructor_ok(self):
        customer = Customer("Raphael", "16149113710")
        date = datetime(2026, 1, 2)
        order = Order(customer, date)