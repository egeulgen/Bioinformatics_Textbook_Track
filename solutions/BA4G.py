import sys
from BA4E import expand, cyclospectrum_mass_peptide


def Score(peptide, spectrum):
    pep_spec = cyclospectrum_mass_peptide(peptide)
    result = 0
    unique_masses = set(pep_spec + spectrum)
    for mass in unique_masses:
        result += min(pep_spec.count(mass), spectrum.count(mass))
    return result


def Trim(leaderboard, spectrum, N):
    if len(leaderboard) <= N:
        return leaderboard

    scores = {}
    for i, peptide in enumerate(leaderboard):
        scores[i] = Score(peptide, spectrum)

    sorted_scores = sorted(scores.values(), reverse=True)
    threshold = sorted_scores[N - 1]

    return [leaderboard[idx] for idx, score in scores.items() if score >= threshold]


def leaderboard_cyclopeptide_sequencing(spectrum, N):
    leaderboard = [[]]
    leader_peptide = []

    while leaderboard:
        leaderboard = expand(leaderboard)
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
    Given: An integer N and a collection of integers Spectrum.
    Return: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).
    '''
    input_lines = sys.stdin.read().splitlines()
    N = int(input_lines[0])
    Spectrum = [int(x) for x in input_lines[1].split()]

    print("-".join(map(str, leaderboard_cyclopeptide_sequencing(Spectrum, N))))
