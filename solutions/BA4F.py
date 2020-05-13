import sys
from BA4C import cyclospectrum


def score(peptide, spectrum):
    pep_spec = cyclospectrum(peptide)
    result = 0
    unique_masses = set(pep_spec + spectrum)
    for mass in unique_masses:
        result += min(pep_spec.count(mass), spectrum.count(mass))
    return result


if __name__ == "__main__":
    '''
    Given: An amino acid string Peptide and a collection of integers Spectrum.
    Return: The score of Peptide against Spectrum, Score(Peptide, Spectrum).
    '''
    input_lines = sys.stdin.read().splitlines()
    Peptide = input_lines[0]
    Spectrum = [int(x) for x in input_lines[1].split()]

    print(score(Peptide, Spectrum))
