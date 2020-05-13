import sys


def convolution(spectrum):
    spectrum.sort()
    conv = []
    for i in range(len(spectrum) - 1):
        for j in range(i, len(spectrum)):
            if spectrum[j] - spectrum[i] != 0:
                conv.append(spectrum[j] - spectrum[i])

    freq_dict = {}
    for mass in set(conv):
        freq_dict[mass] = conv.count(mass)

    sorted_mass_list = [k for k, _ in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)]
    conv = []
    for mass in sorted_mass_list:
        conv += [mass] * freq_dict[mass]
    return conv


if __name__ == "__main__":
    '''
    Given: A collection of integers Spectrum.
    Return: The list of elements in the convolution of Spectrum in decreasing order of their multiplicities. If an 
    element has multiplicity k, it should appear exactly k times.
    '''
    spectrum = [int(x) for x in sys.stdin.readline().strip().split()]

    print(" ".join(map(str, convolution(spectrum))))
