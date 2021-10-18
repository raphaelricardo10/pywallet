from sales import Cashback

class ConstantByTotal(Cashback):
    def __init__(self, percent: float, total: float=None) -> None:
        super().__init__(total, percent)

    def calculateCashback(self) -> float:
        if self.total < 0:
            raise ValueError("The value cannot be less than zero")

        if self.percent < 0:
            raise ValueError("Percent value cannot be less than zero")

        return self.total*self.percent/float(100)