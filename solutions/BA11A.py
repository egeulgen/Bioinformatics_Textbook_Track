import sys
MASS_TABLE = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
INV_MASS_TABLE = {v: k for k, v in MASS_TABLE.items()}


def spectrum_graph(spectrum):
    adj_list = []
    for i in range(len(spectrum)):
        for j in range(i, len(spectrum)):
            if (spectrum[j] - spectrum[i]) in INV_MASS_TABLE:
                adj_list.append([spectrum[i], spectrum[j], INV_MASS_TABLE[spectrum[j] - spectrum[i]]])
    return adj_list


if __name__ == "__main__":
    '''
    Given: A space-delimited list of integers Spectrum.
    Return: Graph(Spectrum).
    '''
    Spectrum = sys.stdin.readline().strip()
    Spectrum = [int(x) for x in Spectrum.split()]
    Spectrum = [0] + Spectrum

    adj_list = spectrum_graph(Spectrum)
    for edge in adj_list:
        print(str(edge[0]) + '->' + str(edge[1]) + ':' + str(edge[2]))