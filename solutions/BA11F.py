import sys
aa_table = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
            'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}


def PeptideVector(peptide):
    prefixMasses = []
    for i in range(len(peptide)):
        prefixMasses.append(sum(peptide[:i + 1]))
    vector = [0] * prefixMasses[-1]
    for mass in prefixMasses:
        vector[mass - 1] = 1
    return vector


def PeptideIdentification(spectral_vector, proteome):
    max_score = -1e6
    mass_list = []
    for aa in proteome:
        mass_list.append(aa_table[aa])

    for i in range(len(mass_list)):
        k = 2
        while i + k < len(mass_list):
            peptide = mass_list[i:i + k]
            pep_vec = PeptideVector(peptide)
            if len(pep_vec) > len(spectral_vector):
                break
            if len(pep_vec) == len(spectral_vector):
                score = 0
                for idx in range(len(pep_vec)):
                    if pep_vec[idx] == 1:
                        score += spectral_vector[idx]
                if score > max_score:
                    max_score = score
                    best_peptide = proteome[i:i + k]
            k += 1
    return best_peptide


if __name__ == "__main__":
    '''
    Given: A space-delimited spectral vector S and an amino acid string Proteome.
    Return: A peptide in Proteome with maximum score against S.
    '''
    tmp = sys.stdin.read().splitlines()
    spectral_vector = [int(x) for x in tmp[0].rstrip().split(' ')]
    proteome = tmp[1].rstrip()

    print(PeptideIdentification(spectral_vector, proteome))

