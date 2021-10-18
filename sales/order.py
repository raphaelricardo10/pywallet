from datetime import datetime
from .product import Product
from .customer import Customer
from .cashback import Cashback

class Order:
    def __init__(self,customer: Customer, sold_at: str, cashback: Cashback=None, items: dict=None) -> None:
        self.customer = customer
        self.sold_at = sold_at
        self.items = []
        self._total = 0
        self._cashbackInstance = cashback

        if items:
            for item in items:
                newProduct = Product(item['type'], float(item['value']))
                self.addItem(newProduct, int(item['qty']))

    @property
    def total(self):
        return self._total

    @property
    def cashback(self):
        return self._cashbackInstance.value

    @property
    def sold_at(self):
        return self._sold_at

    @sold_at.setter
    def sold_at(self, value):
        try:
            self._sold_at = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

            if self._sold_at > datetime.now():
                raise ValueError("The order date is from future")

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

        if self._cashbackInstance:
            self._cashbackInstance.total = self._total