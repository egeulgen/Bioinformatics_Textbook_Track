import sys
from BA3F import parse_adj_list
from BA3F import Eulerian_cycle


def Eulerian_path(adj_list):
    deg_diffs = {}
    for source, targets in adj_list.items():
        if source in deg_diffs:
            deg_diffs[source] += len(targets)
        else:
            deg_diffs[source] = len(targets)
        for target in targets:
            if target in deg_diffs:
                deg_diffs[target] -= 1
            else:
                deg_diffs[target] = -1

    to_add_s = [node for node, diff in deg_diffs.items() if diff == -1][0]
    to_add_t = [node for node, diff in deg_diffs.items() if diff == 1][0]
    if to_add_s in adj_list:
        adj_list[to_add_s].append(to_add_t)
    else:
        adj_list[to_add_s] = [to_add_t]

    cycle = Eulerian_cycle(adj_list)
    idx = 0
    while True:
        if cycle[idx] == to_add_s and cycle[idx + 1] == to_add_t:
            break
        idx += 1
    return cycle[idx + 1:] + cycle[1:idx + 1]


if __name__ == "__main__":
    '''
    Given: A directed graph that contains an Eulerian path, where the graph is given in the form of an adjacency list.
    Return: An Eulerian path in this graph.
    '''
    input_lines = sys.stdin.read().splitlines()
    Adj_list = parse_adj_list(input_lines)

    print("->".join(Eulerian_path(Adj_list)))
