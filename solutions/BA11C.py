import sys
aa_table = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113,
            'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163, 'X': 4, 'Z': 5}


def PeptideVector(peptide):
    prefixMasses = []
    for i in range(len(peptide)):
        prefix = peptide[:i+1]
        mass = 0
        for aa in prefix:
            mass += aa_table[aa]
        prefixMasses.append(mass)

    vector = [0] * prefixMasses[-1]
    for mass in prefixMasses:
        vector[mass - 1] = 1
    return vector


if __name__ == "__main__":
    '''
    Given: A peptide P.
    Return: The peptide vector of P.
    '''
    peptide = sys.stdin.read().rstrip()
    print(' '.join(str(x) for x in PeptideVector(peptide)))