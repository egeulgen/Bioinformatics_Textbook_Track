def ProcessInput(P):
    P = P[1:-1]
    P = P.split(')(')
    for i in range(len(P)):
            P[i] = P[i].split(' ')
            for j in range(len(P[i])):
                P[i][j] = int(P[i][j])
    return P


def ChromosomeToCycle(Chromosome):
    Nodes = []
    for block in Chromosome:
        if block > 0:
            Nodes.append(2 * block - 1)
            Nodes.append(2 * block)
        else:
            Nodes.append(-2 * block)
            Nodes.append(-2 * block - 1)
    return Nodes


def ColoredEdges(P):
    Edges = []
    for Chromosome in P:
        Nodes = ChromosomeToCycle(Chromosome)
        for j in range(1, len(Nodes), 2):
            if j != len(Nodes) - 1:
                Edges.append([Nodes[j], Nodes[j + 1]])
            else:
                Edges.append([Nodes[j], Nodes[0]])
    return Edges


def TwoBreakOnGenomeGraph(GenomeGraph, i1 , i2 , i3 , i4):
    if [i1, i2] in GenomeGraph:
        for i in range(len(GenomeGraph)):
            if GenomeGraph[i] == [i1, i2]:
                GenomeGraph[i] = [i1, i3]
    else:
        for i in range(len(GenomeGraph)):
            if GenomeGraph[i] == [i2, i1]:
                GenomeGraph[i] = [i3, i1]
    if [i3, i4] in GenomeGraph:
        for i in range(len(GenomeGraph)):
            if GenomeGraph[i] == [i3, i4]:
                GenomeGraph[i] = [i2, i4]
    else:
        for i in range(len(GenomeGraph)):
            if GenomeGraph[i] == [i4, i3]:
                GenomeGraph[i] = [i4, i2]
    return GenomeGraph


def CycleToChromosome(Nodes):
    Chromosome = []
    for i in range(0, len(Nodes), 2):
        if Nodes[i] < Nodes[i + 1]:
            Chromosome.append(Nodes[i + 1] // 2)
        else:
            Chromosome.append(-Nodes[i] // 2)
    return Chromosome


def FindNextEdge(current, edges):
    if len(edges) == 0:
        return -1
    idx = 0
    while not (current[1] + 1 == edges[idx][0] or current[1] - 1 == edges[idx][0]):
        idx += 1
        if idx == len(edges):
            return -1
    return edges[idx]


def GraphToGenome(GenomeGraph):
    Q = []
    Cycles = []
    idx = 0
    while len(GenomeGraph) != 0:
        Cycle = []
        current = GenomeGraph[0]
        while current != -1:
            Cycle += current
            GenomeGraph.remove(current)
            current = FindNextEdge(current, GenomeGraph)
        Cycles.append(Cycle)
    for Cycle in Cycles:
        Cycle = Cycle[-3:] + Cycle[:-3]
        Chromosome = CycleToChromosome(Cycle)
        Q.append(Chromosome)
    return Q


def TwoBreakOnGenome(P, i1 , i2 , i3 , i4):
    GenomeGraph = ColoredEdges(P)
    GenomeGraph = TwoBreakOnGenomeGraph(GenomeGraph, i1 , i2 , i3 , i4)
    Q = GraphToGenome(GenomeGraph)
    return Q


if __name__ == "__main__":
    '''
    Given: The colored edges of a genome graph GenomeGraph, followed by indices i, i', j, and j'.
    Return: The colored edges of the genome graph resulting from applying the 2-break operation.
    '''
    P = input().rstrip()
    P = ProcessInput(P)
    i1, i2, i3, i4 = map(int, input().rstrip().split(', '))
    result = TwoBreakOnGenome(P, i1, i2, i3, i4)
    for j in range(len(result)):
        result[j] = '(' + ' '.join(('+' if i > 0 else '') + str(i) for i in result[j]) + ')'
    print(''.join(result))
