import unittest
from sales import Customer, Order, Product

class TestOrderValidationMethods(unittest.TestCase):
    
    def test_total_order_ok(self):
        customer = Customer("Raphael", "16149113710")
        order = Order(customer, "2020-01-02 00:00:00")
        order.addItem(Product("A", 10), 2)
        order.addItem(Product("B", 30), 3)
        self.assertEqual(order.total, 110)

    def test_reassign_total(self):
        customer = Customer("Raphael", "16149113710")
        order = Order(customer, "2020-01-02 00:00:00")
        with self.assertRaises(AttributeError):
            order.total = 150

    def test_constructor_ok(self):
        customer = Customer("Raphael", "16149113710")
        order = Order(customer, "2020-01-02 00:00:00")

    def test_invalid_date(self):
        customer = Customer("Raphael", "16149113710")
        with self.assertRaises(ValueError):
            Order(customer, "1213123-01-02 00:00:00")


    def test_cashback_change(self):
        customer = Customer("Raphael", "16149113710")
        order = Order(customer, "2020-01-02 00:00:00", 5)
        order.addItem(Product("A", 10), 5)
        self.assertEqual(order.cashback, 2.5)
        print(order.cashback)
        order.addItem(Product("A", 20), 3)
        self.assertEqual(order.cashback, 5.5)
        print(order.cashback)