import unittest
from datetime import datetime
from pywallet.product import Product
from pywallet.order import Order
from pywallet.customer import Customer

class TestOrderValidationMethods(unittest.TestCase):
    
    def test_total_order_ok(self):
        customer = Customer("Raphael", "16149113710")
        sold_at = datetime(2026, 1, 2)
        order = Order(customer, sold_at)
        order.addItem(Product("A", 10), 2)
        order.addItem(Product("B", 30), 3)
        
        self.assertEqual(order.total, 110)

    def test_reassign_total(self):
        customer = Customer("Raphael", "16149113710")
        sold_at = datetime(2026, 1, 2)
        order = Order(customer, sold_at)
        with self.assertRaises(AttributeError):
            order.total = 150

    def test_constructor_ok(self):
        customer = Customer("Raphael", "16149113710")
        sold_at = datetime(2026, 1, 2)
        order = Order(customer, sold_at)

    def test_date_validation(self):
        customer = Customer("Raphael", "16149113710")
        with self.assertRaises(ValueError):
            Order(customer, "1213123-01-02 00:00:00")