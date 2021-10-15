class Product:
    def __init__(self, prodType: str, value: float) -> None:
        self.type = prodType
        self.value = value

    def validateValue(value: float) -> None:
        if value < 0:
            raise ValueError

    
