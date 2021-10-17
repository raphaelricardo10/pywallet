from datetime import datetime
from pywallet.product import Product
from pywallet.customer import Customer
from pywallet.cashback import Cashback

class Order:
    def __init__(self, customer: Customer, sold_at: str, cashbackPercent:float =None) -> None:
        self.customer = customer
        self.sold_at = sold_at
        self.items = []
        self._total = 0

        if cashbackPercent:
            self.cashbackInstance = Cashback(self.total, cashbackPercent)
        else:
            self.cashbackInstance = None

    @property
    def total(self):
        return self._total

    @property
    def cashback(self):
        return self.cashbackInstance.value

    @property
    def sold_at(self):
        return self._sold_at

    @sold_at.setter
    def sold_at(self, value):
        try:
            self._sold_at = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise

    class Item:
        def __init__(self, product: Product, qty: int) -> None:
            self.product = product
            self.qty = qty

    def addItem(self, product: Product, qty: int) -> None:
        newItem = Order.Item(product, qty)
        self.items.append(newItem)
        self._total += newItem.product.value * newItem.qty

        if self.cashbackInstance:
            self.cashbackInstance.total = self._total