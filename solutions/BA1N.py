import sys
from BA1G import hamming_dist


def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for suffix in suffix_neighbors:
        if hamming_dist(pattern[1:], suffix) < d:
            for nuc in ['A', 'C', 'G', 'T']:
                neighborhood.add(nuc + suffix)
        else:
            neighborhood.add(pattern[0] + suffix)
    return neighborhood


if __name__ == "__main__":
    '''
    Given: A DNA string Pattern and an integer d.
    Return: The collection of strings Neighbors(Pattern, d).
    '''
    input_lines = sys.stdin.read().splitlines()
    Pattern = input_lines[0]
    d = int(input_lines[1])

    result = neighbors(Pattern, d)
    for r in result:
        print(r)
