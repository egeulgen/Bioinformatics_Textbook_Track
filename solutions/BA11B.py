import sys
aa_table = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
mass_table = {v: k for k, v in aa_table.items()}


def SpectrumGraph(spectrum):
    adj_list = []
    for i in range(len(spectrum)):
        for j in range(i, len(spectrum)):
            if spectrum[j] - spectrum[i] in mass_table.keys():
                adj_list.append([spectrum[i], spectrum[j], mass_table[spectrum[j] - spectrum[i]]])
    return adj_list


def IdealSpectrum(Peptide):
    PrefixMass = [0]
    for i in range(len(Peptide)):
        temp = PrefixMass[i] + aa_table[Peptide[i]]
        PrefixMass.append(temp)
    LinearSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i + 1, len(Peptide) + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
    LinearSpectrum.sort()
    return LinearSpectrum


def Paths(adj_list):
    node = 0
    peptide_list = []
    tmp_edges = []
    peptide = ''
    tmp_peps = []

    while any([len(x) != 0 for x in tmp_edges]) or len(tmp_edges) == 0:
        next_edges = [e for e in adj_list if e[0] == node]
        if len(next_edges) > 1:
            tmp = next_edges[1:]
            tmp_edges.append(tmp)
            tmp_peps.append(peptide)

        next_edge = next_edges[0]
        peptide += next_edge[2]
        node = next_edge[1]

        if len([e for e in adj_list if e[0] == node]) == 0:
            tmp = [x for x in tmp_edges if len(x) != 0][-1]
            next_edge = tmp.pop()
            node = next_edge[1]
            peptide_list.append(peptide)
            tmp_pep = tmp_peps.pop()
            peptide = tmp_pep + next_edge[2]

    return peptide_list


def DecodingIdealSpectrum(spectrum):
    adj_list = SpectrumGraph(spectrum)
    all_paths = Paths(adj_list)
    for peptide in all_paths:
        if set(spectrum).issubset(IdealSpectrum(peptide)):
            return peptide


if __name__ == "__main__":
    '''
    Given: A space-delimited list of integers, Spectrum.
    Return: An amino acid string with an ideal spectrum that matches Spectrum.
    '''
    spectrum = sys.stdin.read().rstrip()
    spectrum = [int(s) for s in spectrum.split()]
    spectrum = [0] + spectrum

    print(DecodingIdealSpectrum(spectrum))