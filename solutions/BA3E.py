import sys


def deBruijn_graph_kmers(patterns):
    adj_list = {}
    for pattern in patterns:
        if pattern[:-1] not in adj_list:
            adj_list[pattern[:-1]] = [pattern[1:]]
        else:
            adj_list[pattern[:-1]].append(pattern[1:])
    return adj_list


if __name__ == "__main__":
    '''
    Given: A collection of k-mers Patterns.
    Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.
    '''
    Patterns = sys.stdin.read().splitlines()

    adj_list = deBruijn_graph_kmers(Patterns)
    for key, val in adj_list.items():
        print(key + ' -> ' + ",".join(val))
