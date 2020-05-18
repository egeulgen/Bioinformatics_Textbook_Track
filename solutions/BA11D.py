import sys
aa_table = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
mass_table = {v: k for k, v in aa_table.items()}
mass_table[4] = 'X'
mass_table[5] = 'Z'


def ConvertPeptideVector(vector):
    prefixMasses = []
    for i in range(len(vector)):
        if vector[i] == 1:
            prefixMasses.append(i + 1)

    peptide = mass_table[prefixMasses[0]]
    for i in range(1, len(prefixMasses)):
        mass = prefixMasses[i] - prefixMasses[i - 1]
        peptide += mass_table[mass]

    return peptide


if __name__ == "__main__":
    '''
    Given: A space-delimited binary vector P.
    Return: A peptide whose binary peptide vector matches P. For masses with more than one amino acid, any choice may 
    be used.
    '''
    vector = [int(x) for x in sys.stdin.read().rstrip().split()]

    print(ConvertPeptideVector(vector))