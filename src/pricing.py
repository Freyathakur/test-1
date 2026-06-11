def format_price(cents: int) -> str:
    # bug: can't concatenate str and float
    return "$" + "{:.2f}".format(cents / 100)
