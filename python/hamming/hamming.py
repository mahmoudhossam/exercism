def distance(strand_a, strand_b):
    if strand_a == strand_b:
        return 0
    elif len(strand_a) != len(strand_b):
        raise ValueError("Strands are of different lengths.")
    diff = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            diff += 1
    return diff
