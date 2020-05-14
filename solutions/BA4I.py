import sys
from BA4H import convolution
from BA4G import Score, Trim


def find_masses(spectrum, M):
    conv = convolution(spectrum)
    conv = [x for x in conv if 57 <= x <= 200]

    freq_dict = {}
    for mass in set(conv):
        freq_dict[mass] = conv.count(mass)

    sorted_elems = sorted(freq_dict.items(), key=lambda kv: kv[1], reverse=True)
    masses = [mass for mass, freq in sorted_elems if freq >= sorted_elems[M][1]]
    masses.sort()
    return masses


def Expand(peptides, masses):
    new_peptides = []
    for pep in peptides:
        for mass in masses:
            new_peptides.append(pep + [mass])
    return new_peptides


def convolution_cyclopeptide_sequencing(spectrum, M, N):
    masses = find_masses(spectrum, M)
    leaderboard = [[]]
    leader_peptide = []

    while leaderboard:
        leaderboard = Expand(leaderboard, masses)
        for peptide in leaderboard:
            if sum(peptide) == spectrum[-1]:
                if Score(peptide, spectrum) > Score(leader_peptide, spectrum):
                    leader_peptide = peptide
            elif sum(peptide) > spectrum[-1]:
                leaderboard = [pep for pep in leaderboard if pep != peptide]
        leaderboard = Trim(leaderboard, spectrum, N)
    return leader_peptide


if __name__ == "__main__":
    '''
    Given: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
    Return: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the 
    convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N 
    (and ties).
    '''
    input_lines = sys.stdin.read().splitlines()
    M = int(input_lines[0])
    N = int(input_lines[1])
    Spectrum = [int(x) for x in input_lines[2].split()]

    print("-".join(map(str, convolution_cyclopeptide_sequencing(Spectrum, M, N))))
