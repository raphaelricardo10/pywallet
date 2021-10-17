from sales import Order
from yaml import load

from sales.customer import Customer

class orderHTTP(Order):
    def __init__(self, response: str, cashbackPercent=None) -> None:

        try:
            obj = load(response)
            customer = Customer(obj['customer']['name'], obj['customer']['document'])

            if not obj['products']:
                raise ValueError("A least one product is required to complete the order")

            super().__init__(customer, obj['sold_at'], items=obj['products'], cashbackPercent=cashbackPercent)

            if float(obj['total']) != self.total:
                raise ValueError("The order total is different of the sum of products")
        
        except:
            raise