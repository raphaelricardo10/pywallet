from pywallet.product import Product

class Order:
    def __init__(self) -> None:
        self.items = []
        self._total = 0

    @property
    def total(self):
        return self._total

    class Item:
        def __init__(self, product: Product, qty: int) -> None:
            self.product = product
            self.qty = qty

    def addItem(self, product: Product, qty: int) -> None:
        newItem = Order.Item(product, qty)
        self.items.append(newItem)
        self._total += newItem.product.value * newItem.qty