from sales import Order
from json import loads

from sales.customer import Customer

class orderHTTP(Order):
    def __init__(self, response: str, cashbackPercent=None) -> None:
        obj = loads(response)
        customer = Customer(obj['customer']['name'], obj['customer']['document'])
        super().__init__(customer, obj['sold_at'], items=obj['products'], cashbackPercent=cashbackPercent)