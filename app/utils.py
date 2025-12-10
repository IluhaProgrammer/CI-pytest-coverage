def discount_price(price: float, disc_percent: float) -> float:
    if not (0 <= disc_percent <= 100):
        raise ValueError(
            "Discount percent must be between 0 and 100"
        )
    return round(
        price * (1 - disc_percent / 100), 2
    )