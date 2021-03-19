def convert(n: int) -> str:
    msg = ""

    if n % 3 == 0:
        msg += "Pling"
    if n % 5 == 0:
        msg += "Plang"
    if n % 7 == 0:
        msg += "Plong"

    return msg or str(n)
