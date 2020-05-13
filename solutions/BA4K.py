import sys
from BA4J import LinearSpectrum


def linear_score(peptide, spectrum):
    pep_spec = LinearSpectrum(peptide)
    result = 0
    unique_masses = set(pep_spec + spectrum)
    for mass in unique_masses:
        result += min(pep_spec.count(mass), spectrum.count(mass))
    return result


if __name__ == "__main__":
    '''
    Given: An amino acid string Peptide and a collection of integers LinearSpectrum.
    Return: The linear score of Peptide against Spectrum, LinearScore(Peptide, Spectrum).
    '''
    input_lines = sys.stdin.read().splitlines()
    Peptide = input_lines[0]
    Spectrum = [int(x) for x in input_lines[1].split()]

    print(linear_score(Peptide, Spectrum))
