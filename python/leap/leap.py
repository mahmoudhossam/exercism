def divisible(x, y):
    return x % y == 0


def is_leap_year(year):
    if divisible(year, 4):
        if divisible(year, 400) or not divisible(year, 100):
            return True
    return False
