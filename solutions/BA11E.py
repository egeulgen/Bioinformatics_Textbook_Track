import sys
aa_table = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
            'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
mass_table = {v: k for k, v in aa_table.items()}


def PeptideSequencing(spectral_vector):
    spectral_vector = [0] + spectral_vector

    adj_list = []
    for i in range(len(spectral_vector)):
        for j in range(i, len(spectral_vector)):
            if (j - i) in mass_table.keys():
                adj_list.append([i, j])

    adj_dict = {}
    for i in range(len(spectral_vector)):
        for j in range(i, len(spectral_vector)):
            if (j - i) in mass_table.keys():
                tmp = [i, mass_table[j - i]]
                if not j in adj_dict.keys():
                    adj_dict[j] = [tmp]
                else:
                    adj_dict[j].append(tmp)

    scores = {0: [0, '-']}
    for node in adj_dict.keys():
        scores[node] = [-1e6, '-']
        tmp = adj_dict[node]
        for x in tmp:
            if x[0] != 0:
                scores[x[0]] = [-1e6, '-']

    for node in adj_dict.keys():
        max_score = -1e6
        bold_edge = '-'
        for parent in adj_dict[node]:
            score = scores[parent[0]][0]
            if score > max_score:
                max_score = score
                bold_edge = parent
        scores[node] = [max_score + spectral_vector[node], bold_edge]

    node = list(scores.keys())[-1]
    peptide = ''
    while node != 0:
        peptide = scores[node][1][1] + peptide
        node = scores[node][1][0]

    return peptide


if __name__ == "__main__":
    '''
    Given: A space-delimited spectral vector S.
    Return: A peptide with maximum score against S. For masses with more than one amino acid, any choice may be used.
    '''
    spectral_vector = [int(x) for x in sys.stdin.read().rstrip().split(' ')]

    print(PeptideSequencing(spectral_vector))
