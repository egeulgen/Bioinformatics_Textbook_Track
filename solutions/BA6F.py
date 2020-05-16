import sys


def chromosome_to_cycle(Chromosome):
    Nodes = []
    for block in Chromosome:
        if block > 0:
            Nodes.append(2 * block - 1)
            Nodes.append(2 * block)
        else:
            Nodes.append(-2 * block)
            Nodes.append(-2 * block - 1)
    return Nodes


if __name__ == "__main__":
    '''
    Given: A chromosome Chromosome containing n synteny blocks.
    Return: The sequence Nodes of integers between 1 and 2n resulting from applying ChromosomeToCycle to Chromosome.
    '''
    Chromosome = sys.stdin.readline().strip()
    Chromosome = Chromosome.replace("(", "").replace(")", "")
    Chromosome = [int(x) for x in Chromosome.split()]

    cycle = chromosome_to_cycle(Chromosome)
    print("(" + " ".join(map(str, cycle)) + ")")