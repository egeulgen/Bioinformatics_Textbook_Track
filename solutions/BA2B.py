import sys
from BA1G import hamming_dist
from BA1K import generate_all_kmers


def distance(pattern, text):
    k = len(pattern)
    min_dist = float("Inf")
    for i in range(len(text) - k + 1):
        dist = hamming_dist(text[i:i + k], pattern)
        if dist < min_dist:
            min_dist = dist
    return min_dist


def median_string(dna_list, k):
    all_kmers = generate_all_kmers(k)

    min_dist = float("Inf")
    for kmer in all_kmers:
        dist = 0
        for dna in dna_list:
            dist += distance(kmer, dna)
        if dist < min_dist:
            min_dist = dist
            med_str = kmer
    return med_str


if __name__ == "__main__":
    '''
    Given: An integer k and a collection of strings Dna.
    Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern. (If multiple answers exist, 
    you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])
    DNA_list = input_lines[1:]

    print(median_string(DNA_list, k))
