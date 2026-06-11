from tabulate import tabulate


def as_table(rows: list[list[str]]) -> str:
    return tabulate(rows, headers="firstrow")
