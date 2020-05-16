import sys
from BA6F import chromosome_to_cycle


def colored_edges(P):
    Edges = list()
    for chromosome in P:
        Nodes = chromosome_to_cycle(chromosome)
        for j in range(1, len(Nodes), 2):
            if j != len(Nodes) - 1:
                Edges.append([Nodes[j], Nodes[j + 1]])
            else:
                Edges.append([Nodes[j], Nodes[0]])
    return Edges


if __name__ == "__main__":
    '''
    Given: A genome P.
    Return: The collection of colored edges in the genome graph of P in the form (x, y).
    '''
    P = sys.stdin.readline().strip()
    P = P[1:-1]
    P = P.split(')(')

    for i in range(len(P)):
        P[i] = [int(x) for x in P[i].split(' ')]

    result = colored_edges(P)
    for j in range(len(result)):
        result[j] = '(' + ', '.join(str(i) for i in result[j]) + ')'
    print(', '.join(result))
