from sales import Order
from yaml import load

from sales.customer import Customer

class orderHTTP(Order):
    def __init__(self, response: str, cashbackPercent=None) -> None:
        obj = load(response)
        customer = Customer(obj['customer']['name'], obj['customer']['document'])
        super().__init__(customer, obj['sold_at'], items=obj['products'], cashbackPercent=cashbackPercent)