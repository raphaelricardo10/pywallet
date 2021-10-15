def calculateCashback(value: float, percent: float) -> float:
    if percent < 0:
        raise ValueError("Percent value cannot be less than zero")

    return value*percent/float(100)