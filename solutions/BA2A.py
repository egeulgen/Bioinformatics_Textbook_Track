import sys
from BA1G import hamming_dist
from BA1N import neighbors


def count_approx_pattern(text, pattern, d):
    k = len(pattern)
    count = 0
    for i in range(len(text) - k + 1):
        if hamming_dist(text[i:i+k], pattern) <= d:
            count += 1
    return count


def motif_enumeration(dna_list, k, d):
    patterns = set()
    for dna in dna_list:
        for i in range(len(dna) - k + 1):
            pattern = dna[i:i + k]
            neighborhood = neighbors(pattern, d)
            for neighbor in neighborhood:
                if all(count_approx_pattern(pat, neighbor, d) > 0 for pat in dna_list):
                    patterns.add(neighbor)
    return patterns


if __name__ == "__main__":
    '''
    Given: Integers k and d, followed by a collection of strings Dna.
    Return: All (k, d)-motifs in Dna.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, d = [int(x) for x in input_lines[0].split()]
    DNA_list = input_lines[1:]

    print(" ".join(motif_enumeration(DNA_list, k, d)))
