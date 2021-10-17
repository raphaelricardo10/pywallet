class Product:
    def __init__(self, prodType: str, value: float) -> None:
        self.type = prodType
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            Product.validateValue(value)
        except:
            raise

        self._value = value


    def validateValue(value: float) -> None:
        if value < 0:
            raise ValueError

    
