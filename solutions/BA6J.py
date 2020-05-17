def TwoBreakOnGenomeGraph(GenomeGraph, i1 , i2 , i3 , i4):
    if [i1, i2] in GenomeGraph:
        GenomeGraph.remove([i1, i2])
    else:
        GenomeGraph.remove([i2, i1])
    if [i3, i4] in GenomeGraph:
        GenomeGraph.remove([i3, i4])
    else:
        GenomeGraph.remove([i4, i3])
    GenomeGraph += [[i1, i3]] + [[i2, i4]]
    return GenomeGraph


if __name__ == "__main__":
    '''
    Given: The colored edges of a genome graph GenomeGraph, followed by indices i, i', j, and j'.
    Return: The colored edges of the genome graph resulting from applying the 2-break operation.
    '''
    GenomeGraph = input().rstrip()
    GenomeGraph = GenomeGraph[1:-1]
    GenomeGraph = GenomeGraph.split('), (')
    for i in range(len(GenomeGraph)):
        GenomeGraph[i] = GenomeGraph[i].split(', ')
        for j in range(len(GenomeGraph[i])):
            GenomeGraph[i][j] = int(GenomeGraph[i][j])
    i1, i2, i3, i4 = map(int, input().rstrip().split(', '))
    result = TwoBreakOnGenomeGraph(GenomeGraph, i1, i2, i3, i4)
    for j in range(len(result)):
        result[j] = '(' + ', '.join(str(i) for i in result[j]) + ')'
    print(', '.join(result))