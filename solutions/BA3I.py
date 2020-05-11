import sys
from BA3E import deBruijn_graph_kmers
from BA3F import Eulerian_cycle


def k_universal_circular_string(k):
    kmers = []
    for i in range(2 ** k):
        kmer = str(bin(i))[2:]
        if len(kmer) != k:
            kmer = '0' * (k - len(kmer)) + kmer
        kmers.append(kmer)

    adj_list = deBruijn_graph_kmers(kmers)
    cycle = Eulerian_cycle(adj_list)

    cycle = cycle[:len(cycle) - k + 1]
    string = cycle[0][:-1]
    for r in cycle:
        string += r[-1]
    return string


if __name__ == "__main__":
    '''
    Given: An integer k.
    Return: A k-universal circular string. (If multiple answers exist, you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])

    print(k_universal_circular_string(k))
