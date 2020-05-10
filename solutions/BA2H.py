import sys
from BA1G import hamming_dist


def distance(pattern, text):
    k = len(pattern)
    min_dist = float("Inf")
    for i in range(len(text) - k + 1):
        dist = hamming_dist(text[i:i + k], pattern)
        if dist < min_dist:
            min_dist = dist
    return min_dist


def DistanceBetweenPatternAndStrings(dna_list, pattern):
    dist = 0
    for dna in dna_list:
        dist += distance(pattern, dna)
    return dist


if __name__ == "__main__":
    '''
    Given: A DNA string Pattern and a collection of DNA strings Dna.
    Return: DistanceBetweenPatternAndStrings(Pattern, Dna).
    '''
    input_lines = sys.stdin.read().splitlines()
    Pattern = input_lines[0]
    DNA_list = input_lines[1].split()

    print(DistanceBetweenPatternAndStrings(DNA_list, Pattern))
