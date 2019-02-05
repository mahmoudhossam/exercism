from collections import Counter
import re


def word_count(phrase):
    words = re.split(r"[^a-zA-Z1-9']", phrase)
    for i, word in enumerate(words):
        if word and word[0] == "'" and word[-1] == "'":
            word = word[1:-1]
        words[i] = word.lower()
    words = filter(None, words)
    c = Counter(words)
    return c
