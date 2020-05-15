import sys


def ManhattanTouristProblem(n, m, Down, Right):
    S = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        S[i][0] = S[i - 1][0] + Down[i - 1][0]
    for j in range(1, m + 1):
        S[0][j] = S[0][j - 1] + Right[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j] + Down[i - 1][j], S[i][j - 1] + Right[i][j - 1])

    return S[n][m]


if __name__ == "__main__":
    '''
    Given: Integers n and m, followed by an n × (m+1) matrix Down and an (n+1) × m matrix Right. The two matrices are 
    separated by the "-" symbol.
    Return: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid whose edges are 
    defined by the matrices Down and Right.
    '''
    input_lines = sys.stdin.read().splitlines()
    n, m = [int(x) for x in input_lines[0].split()]

    Down = []
    for idx in range(1, n + 1):
        Down.append([int(x) for x in input_lines[idx].split()])

    Right = []
    for idx in range(n + 2, len(input_lines)):
        Right.append([int(x) for x in input_lines[idx].split()])


    print(ManhattanTouristProblem(m, m, Down, Right))
