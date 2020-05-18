import sys

aa_table = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
            'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
masses = list(aa_table.values())


def SpectralDictionarySize(spectral_vector, threshold, max_score):
    m = len(spectral_vector)

    Size = {}
    Size[0] = {}
    Size[0][0] = 1

    for t in range(1, max_score + 1):
        Size[0][t] = 0

    for i in range(1, m + 1):
        Size[i] = {}
        for t in range(max_score + 1):
            Size[i][t] = 0
            for a in masses:
                if (i - a) >= 0 and (t - spectral_vector[i - 1]) >= 0 and (t - spectral_vector[i - 1]) <= max_score:
                    Size[i][t] += Size[i - a][t - spectral_vector[i - 1]]

    final_size = 0
    for t in range(threshold, max_score + 1):
        final_size += Size[m][t]

    return final_size


if __name__ == "__main__":
    '''
    Given: A spectral vector Spectrum', an integer threshold, and an integer max_score.
    Return: The size of the dictionary Dictionarythreshold(Spectrum').
    '''
    tmp = sys.stdin.read().splitlines()
    spectral_vector = [int(x) for x in tmp[0].rstrip().split(' ')]
    threshold = int(tmp[1])
    max_score = int(tmp[2])

    print(SpectralDictionarySize(spectral_vector, threshold, max_score))