import re


def verify(isbn):
    if not isbn:
        return False
    isbn = isbn.replace("-", "")
    invalid_char = re.findall(r"[A-Z]", isbn[:-1])
    control_character = re.findall(r"X|\d", isbn[-1])
    if invalid_char or not control_character or len(isbn) != 10:
        return False
    else:
        result = 0
        for i in range(10, 0, -1):
            digit = isbn[i - 1]
            if digit == "X":
                digit = 10
            result += int(digit) * i
        return result % 11 == 0
