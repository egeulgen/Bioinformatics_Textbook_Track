import sys


def overlap_graph(patterns):
    adj_list = []
    for i in range(len(patterns) - 1):
        for j in range(i, len(patterns)):
            if patterns[i][1:] == patterns[j][:-1]:
                adj_list.append((patterns[i], patterns[j]))
            if patterns[j][1:] == patterns[i][:-1]:
                adj_list.append((patterns[j], patterns[i]))
    return adj_list


if __name__ == "__main__":
    '''
    Given: A collection Patterns of k-mers.
    Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
    '''
    Patterns = sys.stdin.read().splitlines()

    adj_list = overlap_graph(Patterns)
    for edge in adj_list:
        print(" -> ".join(edge))
