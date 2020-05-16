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


def FindNextEdge(current, edges):
    if len(edges) == 0:
        return -1
    idx = 0
    while not (current[0] in edges[idx] or current[1] in edges[idx]):
        idx += 1
        if idx == len(edges):
            return -1
    return edges[idx]


def FindCycles(edges):
    Cycles = []
    while len(edges) != 0:
        start = edges[0]
        edges.remove(edges[0])
        Cycle = [start]
        current = FindNextEdge(start, edges)
        while current != -1:
            Cycle.append(current)
            edges.remove(current)
            current = FindNextEdge(current, edges)
        if len(Cycle) > 2:
            Cycles.append(Cycle)
    return Cycles


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


def TwoBreakOnGenome(P, i1 , i2 , i3 , i4):
    GenomeGraph = ColoredEdges(P)
    GenomeGraph = TwoBreakOnGenomeGraph(GenomeGraph, i1, i2, i3, i4)
    Q = GraphToGenome(GenomeGraph)
    return Q


def FindNextEdge2(current, edges):
    if len(edges) == 0:
        return -1
    idx = 0
    val = current[1]
    if val % 2 == 0:
        val -= 1
    else:
        val += 1
    while not val in edges[idx]:
        idx += 1
        if idx == len(edges):
            return -1
    if val == edges[idx][1]:
        edges[idx].reverse()
    return edges[idx]


def CycleToChromosome(Nodes):
    Chromosome = []
    for i in range(0, len(Nodes), 2):
        if Nodes[i] < Nodes[i + 1]:
            Chromosome.append(Nodes[i + 1] // 2)
        else:
            Chromosome.append(-Nodes[i] // 2)
    return Chromosome


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
            next_edge = FindNextEdge2(current, GenomeGraph)
            current = next_edge
        Cycles.append(Cycle)
    for Cycle in Cycles:
        Cycle = [Cycle[-1]] + Cycle[:-1]
        Chromosome = CycleToChromosome(Cycle)
        Q.append(Chromosome)
    return Q


def ShortestRearrangementScenario(P, Q):
    result = [P]
    RedEdges = ColoredEdges(P)
    BlueEdges = ColoredEdges(Q)
    BreakpointGraph = BlueEdges + RedEdges
    NonTrivialCycles = FindCycles(BreakpointGraph)
    while len(NonTrivialCycles) != 0:
        Cycle = NonTrivialCycles[0]
        for i in range(len(Cycle) - 1):
            if Cycle[i][0] in Cycle[i + 1]:
                Cycle[i].reverse()
            if Cycle[i + 1][1] in Cycle[i]:
                Cycle[i+1].reverse()
        idx = 0
        while not Cycle[idx] in RedEdges:
            idx += 1
        i1, i2 = Cycle[idx]
        if idx + 2 != len(Cycle):
            i3, i4 = Cycle[idx + 2]
        else:
            i3, i4 = Cycle[0]
        RedEdges.remove([i1, i2])
        RedEdges.remove([i3, i4])
        RedEdges.append([i1, i4])
        RedEdges.append([i2, i3])
        BreakpointGraph = BlueEdges + RedEdges
        NonTrivialCycles = FindCycles(BreakpointGraph)
        P = TwoBreakOnGenome(P, i1 , i2 , i4 , i3)
        result.append(P)
    return result

if __name__ == "__main__":
    '''
    Given: Two genomes with circular chromosomes on the same set of synteny blocks.
    Return: The sequence of genomes resulting from applying a shortest sequence of 2-breaks transforming one genome into
    the other.
    '''
    P = input().rstrip()
    P = ProcessInput(P)
    Q = input().rstrip()
    Q = ProcessInput(Q)
    answer = ShortestRearrangementScenario(P, Q)
    for result in answer:
        for j in range(len(result)):
            result[j] = '(' + ' '.join(('+' if i > 0 else '') + str(i) for i in result[j]) + ')'
        print(''.join(result))