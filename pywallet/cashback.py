def calculateCashback(value: float, percent: float) -> float:
    if value < 0:
        raise ValueError("The value cannot be less than zero")

    if percent < 0:
        raise ValueError("Percent value cannot be less than zero")

    return value*percent/float(100)