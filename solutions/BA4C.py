import sys
MASS_TABLE = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}


def cyclospectrum(peptide):
    full_mass = 0
    for aa in peptide:
        full_mass += MASS_TABLE[aa]
    spec = [0, full_mass]
    temp = peptide + peptide
    for k in range(1, len(peptide)):
        for i in range(len(peptide)):
            subpeptide = temp[i:i + k]
            mass = 0
            for aa in subpeptide:
                mass += MASS_TABLE[aa]
            spec.append(mass)
    spec.sort()
    return spec


if __name__ == "__main__":
    '''
    Given: An amino acid string Peptide.
    Return: Cyclospectrum(Peptide).
    '''
    Peptide = sys.stdin.readline().strip()

    print(" ".join(map(str, cyclospectrum(Peptide))))
