class Cashback:
    def __init__(self, total: float, percent: float) -> None:
        self._percent = percent
        self.total = total

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value):
        if value < 0:
            raise ValueError("The percent cannot be less than zero")
            
        self._percent = value
        self.value = Cashback.calculateCashback(self.total, self.percent)

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if value < 0:
            raise ValueError("The total cannot be less than zero")
        
        self._total = value
        self.value = Cashback.calculateCashback(self.total, self.percent)

    def calculateCashback(total: float, percent: float) -> float:
        if total < 0:
            raise ValueError("The value cannot be less than zero")

        if percent < 0:
            raise ValueError("Percent value cannot be less than zero")

        return total*percent/float(100)