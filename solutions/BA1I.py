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


def most_freq_kmers_mismatch(text, k, d):
    count_dict = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        neighborhood = neighbors(kmer, d)
        for approx_pattern in neighborhood:
            if approx_pattern in count_dict:
                count_dict[approx_pattern] += 1
            else:
                count_dict[approx_pattern] = 1
    max_freq = max(count_dict.values())
    return [kmer for kmer, count in count_dict.items() if count == max_freq]


if __name__ == "__main__":
    '''
    Given: A string Text as well as integers k and d.
    Return: All most frequent k-mers with up to d mismatches in Text.
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    k, d = [int(x) for x in input_lines[1].split()]

    print(" ".join(most_freq_kmers_mismatch(Text, k, d)))
