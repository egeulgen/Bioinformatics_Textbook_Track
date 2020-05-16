import sys
from BA6H import colored_edges


def find_next_edge(current, edges):
    if len(edges) == 0:
        return -1
    idx = 0
    while not (current[0] in edges[idx] or current[1] in edges[idx]):
        idx += 1
        if idx == len(edges):
            return -1
    return edges[idx]


def two_break_distance(P, Q):
    edgesP = colored_edges(P)
    edgesQ = colored_edges(Q)
    edges = edgesP + edgesQ
    blocks = set()
    for edge in edges:
        blocks.add(edge[0])
        blocks.add(edge[1])
    Cycles = []
    while len(edges) != 0:
        start = edges[0]
        edges.remove(edges[0])
        Cycle = [start]
        current = find_next_edge(start, edges)
        while current != -1:
            Cycle.append(current)
            edges.remove(current)
            current = find_next_edge(current, edges)
        Cycles.append(Cycle)
    return len(blocks) // 2 - len(Cycles)


if __name__ == "__main__":
    '''
    Given: Two genomes with circular chromosomes on the same set of synteny blocks.
    Return: The 2-break distance between these two genomes.
    '''
    input_lines = sys.stdin.read().splitlines()
    P = input_lines[0]
    P = P[1:-1]
    P = P.split(')(')
    for i in range(len(P)):
        P[i] = [int(x) for x in P[i].split(' ')]

    Q = input_lines[1]
    Q = Q[1:-1]
    Q = Q.split(')(')
    for i in range(len(Q)):
        Q[i] = [int(x) for x in Q[i].split(' ')]

    print(two_break_distance(P, Q))
