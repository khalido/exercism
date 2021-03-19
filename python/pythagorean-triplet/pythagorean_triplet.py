"""
need to add some maths to speed this up, the solution below is very slow.
"""

# %%
def triplets_with_sum(number: int) -> list:
    triplets = []

    for a in range(1, number // 3):
        for b in range(a + 1, number // 2):
            c = number - a - b

            if (a + b >= c) and (a ** 2 + b ** 2 == c ** 2):
                triplets.append([a, b, c])

    return triplets