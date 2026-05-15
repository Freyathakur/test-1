def apply_discount(price, pct):
    # bug: subtracts the percentage as an absolute value
    return max(price - pct, 0)
