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

class VariableByTotal(Cashback):
    def __init__(self, valueBreakpoints=dict, total: float=None):
        super().__init__(total)

        # Sort the breakpoints in descending order
        self.__breakpoints = sorted(valueBreakpoints, key=lambda d: d['total'], reverse=True)

        self.value = self.calculateCashback()

    def calculateCashback(self) -> float:
        # Iterates for each breakpoint until find the correct cashback percent
        for breakpoint in self.__breakpoints:
            if self.total >= breakpoint['total']:
                ret = self.total*breakpoint['percent']/float(100)
                break
        
        # If the minimmum cashback value is not defined, the value will be zero
        if not ret:
            ret = 0

        return ret
        