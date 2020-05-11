import sys
from BA3E import deBruijn_graph_kmers
from BA3G import Eulerian_path


def string_reconstruction(patterns):
    adj_list = deBruijn_graph_kmers(patterns)
    path = Eulerian_path(adj_list)
    ReconstructedString = path[0][:-1]
    for r in path:
        ReconstructedString += r[-1]
    return ReconstructedString


if __name__ == "__main__":
    '''
    Given: An integer k followed by a list of k-mers Patterns.
    Return: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])
    Patterns = input_lines[1:]

    print(string_reconstruction(Patterns))
