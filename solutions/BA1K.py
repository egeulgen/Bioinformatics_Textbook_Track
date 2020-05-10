import sys
from BA1A import count_pattern


def generate_all_kmers(k):
    if k == 1:
        return ["A", "C", "G", "T"]
    kmers = []
    suff = generate_all_kmers(k - 1)
    for nuc in ["A", "C", "G", "T"]:
        for s in suff:
            kmers.append(nuc + s)
    return kmers


def frequency_array(text, k):
    all_kmers = generate_all_kmers(k)
    freq_arr = []
    for kmer in all_kmers:
        freq_arr.append(count_pattern(text, kmer))
    return freq_arr


if __name__ == "__main__":
    '''
    Given: A DNA string Text and an integer k.
    Return: The frequency array of k-mers in Text.
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    k = int(input_lines[1])

    print(" ".join(map(str, frequency_array(Text, k))))
