import sys
from BA3E import deBruijn_graph_kmers
from BA3M import maximal_non_branching_paths


def contig_generation(kmers):
    adj_list = deBruijn_graph_kmers(kmers)
    paths = maximal_non_branching_paths(adj_list)
    contigs = []
    for path in paths:
        contig = path[0]
        for edge in path[1:]:
            contig += edge[-1]
        contigs.append(contig)
    return contigs


if __name__ == "__main__":
    '''
    Given: A collection of k-mers Patterns.
    Return: All contigs in DeBruijn(Patterns). (You may return the strings in any order.)
    '''
    Patterns = sys.stdin.read().splitlines()
    contigs = contig_generation(Patterns)
    contigs.sort()
    print(" ".join(contigs))
