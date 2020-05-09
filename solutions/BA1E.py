import sys


def most_freq_kmers(text, k, t):
    count_dict = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        if kmer not in count_dict:
            count_dict[kmer] = 1
        else:
            count_dict[kmer] += 1

    max_freq = max(count_dict.values())
    if max_freq < t:
        return []
    return [kmer for kmer, count in count_dict.items() if count == max_freq]


def find_clumping_kmers(text, k, L, t):
    result = set()
    for i in range(len(text) - L + 1):
        window = text[i:i + L]
        win_kmers = most_freq_kmers(window, k, t)
        for kmer in win_kmers:
            result.add(kmer)
    return result


if __name__ == "__main__":
    '''
    Given: A string Genome, and integers k, L, and t.
    Return: All distinct k-mers forming (L, t)-clumps in Genome.
    '''
    input_lines = sys.stdin.read().splitlines()
    Genome = input_lines[0]
    k, L, t = [int(x) for x in input_lines[1].split()]

    print(" ".join(find_clumping_kmers(Genome, k, L, t)))
