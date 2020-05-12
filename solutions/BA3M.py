import sys
from BA3F import parse_adj_list, remove_edge


def maximal_non_branching_paths(adj_list):
    paths = []

    # in and out degrees
    in_out_degrees = {}
    for source, targets in adj_list.items():
        if source not in in_out_degrees:
            in_out_degrees[source] = [0, len(targets)]
        else:
            in_out_degrees[source][1] += len(targets)

        for target in targets:
            if target not in in_out_degrees:
                in_out_degrees[target] = [1, 0]
            else:
                in_out_degrees[target][0] += 1

    # find all non-branching paths
    for v in list(in_out_degrees):
        if in_out_degrees[v] != [1, 1]:
            if in_out_degrees[v][1] > 0:
                while v in adj_list:
                    w = adj_list[v][0]
                    non_branching_path = [v, w]
                    adj_list = remove_edge(adj_list, v, w)
                    while in_out_degrees[w] == [1, 1]:
                        u = adj_list[w][0]
                        non_branching_path.append(u)
                        adj_list = remove_edge(adj_list, w, u)
                        w = u
                    paths.append(non_branching_path)

    # find isolated cycles
    while adj_list:
        start_node = list(adj_list)[0]
        current_node = adj_list[start_node][0]
        adj_list = remove_edge(adj_list, start_node, current_node)
        cycle = [start_node, current_node]
        while current_node != start_node:
            target_node = adj_list[current_node][0]
            cycle.append(target_node)
            adj_list = remove_edge(adj_list, current_node, target_node)
            current_node = target_node
        paths.append(cycle)

    return paths


if __name__ == "__main__":
    '''
    Given: The adjacency list of a graph whose nodes are integers.
    Return: The collection of all maximal non-branching paths in the graph.
    '''
    input_lines = sys.stdin.read().splitlines()
    Adj_list = parse_adj_list(input_lines)

    result = maximal_non_branching_paths(Adj_list)
    for r in result:
        print("->".join(r))
