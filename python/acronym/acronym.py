import re
import string


def abbreviate(words):
    parts = re.split("( |-|_)", words)
    return "".join(
        [
            initial[0]
            for initial in parts
            if initial.strip() and initial[0] in string.ascii_letters
        ]
    ).upper()
