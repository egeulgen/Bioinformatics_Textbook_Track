import sys
from BA4K import linear_score


def Trim(leaderboard, spectrum, N):
    if len(leaderboard) <= N:
        return leaderboard

    scores = {}
    for i, peptide in enumerate(leaderboard):
        scores[i] = linear_score(peptide, spectrum)

    sorted_scores = sorted(scores.values(), reverse=True)
    threshold = sorted_scores[N - 1]

    return [leaderboard[idx] for idx, score in scores.items() if score >= threshold]


if __name__ == "__main__":
    '''
    Given: A leaderboard of linear peptides Leaderboard, a linear spectrum Spectrum, and an integer N.
    Return: The top N peptides from Leaderboard scored against Spectrum. Remember to use LinearScore.
    '''
    input_lines = sys.stdin.read().splitlines()
    Leaderboard = input_lines[0].split()
    Spectrum = [int(x) for x in input_lines[1].split()]
    N = int(input_lines[2])

    print(" ".join(Trim(Leaderboard, Spectrum, N)))
