import sys


def LCS(v, w):
    v = '-' + v
    w = '-' + w

    S = [[0 for _ in range(len(w))] for _ in range(len(v))]
    Backtrack = [[None for _ in range(len(w))] for _ in range(len(v))]

    for i in range(1, len(v)):
        for j in range(1, len(w)):
            tmp = S[i - 1][j - 1] + (1 if v[i] == w[j] else 0)
            S[i][j] = max(S[i - 1][j], S[i][j - 1], tmp)

            if S[i][j] == S[i - 1][j]:
                Backtrack[i][j] = "up"
            elif S[i][j] == S[i][j - 1]:
                Backtrack[i][j] = "left"
            else:
                Backtrack[i][j] = "diag"

    LCS = ""
    while i > 0 and j > 0:
        if Backtrack[i][j] == "diag":
            LCS = v[i] + LCS
            i -= 1
            j -= 1
        elif Backtrack[i][j] == "left":
            j -= 1
        else:
            i -= 1

    return LCS


if __name__ == "__main__":
    '''
    Given: Two strings.
    Return: A longest common subsequence of these strings.
    '''
    input_lines = sys.stdin.read().splitlines()
    s = input_lines[0]
    t = input_lines[1]

    print(LCS(s,t))