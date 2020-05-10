import sys
from BA1C import rev_comp
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


def most_freq_kmers_mismatch_revc(text, k, d):
    count_dict = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        neighborhood = neighbors(kmer, d)
        for approx_pattern in neighborhood:
            if approx_pattern in count_dict:
                count_dict[approx_pattern] += 1
            else:
                count_dict[approx_pattern] = 1
            r_pattern = rev_comp(approx_pattern)
            if r_pattern in count_dict:
                count_dict[r_pattern] += 1
            else:
                count_dict[r_pattern] = 1
    max_freq = max(count_dict.values())
    return [kmer for kmer, count in count_dict.items() if count == max_freq]


if __name__ == "__main__":
    '''
    Given: A DNA string Text as well as integers k and d.
    Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible 
    k-mers.
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    k, d = [int(x) for x in input_lines[1].split()]

    print(" ".join(most_freq_kmers_mismatch_revc(Text, k, d)))
