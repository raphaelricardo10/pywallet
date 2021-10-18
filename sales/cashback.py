from abc import ABCMeta, abstractmethod

class Cashback(metaclass=ABCMeta):
    def __init__(self, total: float=None, percent: float=None) -> None:
            self._percent = percent
            self._total = total

            if total and percent and True:
                self.value = self.calculateCashback()

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value):
        if value < 0:
            raise ValueError("The percent cannot be less than zero")
            
        self._percent = value
        self.value = self.calculateCashback()

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if value < 0:
            raise ValueError("The total cannot be less than zero")
        
        self._total = value
        self.value = self.calculateCashback()

    @abstractmethod
    def calculateCashback(self):
        pass