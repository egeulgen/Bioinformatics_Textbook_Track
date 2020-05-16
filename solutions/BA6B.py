import sys


def number_of_breakpoints(P):
    P = [0] + P
    P.append(max(P) + 1)
    num_bp = 0
    for i in range(1, len(P) - 1):
        if P[i] != P[i - 1] + 1:
            num_bp += 1
    return num_bp


if __name__ == "__main__":
    '''
    Given: A signed permutation P.
    Return: The number of breakpoints in P.
    '''
    P = sys.stdin.readline().strip()
    P = P.replace("(", "").replace(")", "")
    P = [int(x) for x in P.split()]

    print(number_of_breakpoints(P))
