import sys


def kSortingReversal(P, k):
    j = k
    while P[j] != k + 1 and P[j] != -(k + 1):
        j += 1
    P[k:j+1] = list(map(lambda x: -x, P[k:j+1][::-1]))
    return P


def GreedySorting(P):
    reversals = []
    for k in range(len(P)):
        while P[k] != k + 1:
            P = kSortingReversal(P, k)
            reversals.append(list(P))
    return reversals


if __name__ == "__main__":
    '''
    Given: A signed permutation P.
    Return: The sequence of permutations corresponding to applying GreedySorting to P, ending with the identity 
    permutation.
    '''
    P = sys.stdin.readline().strip()
    P = P.replace("(", "").replace(")", "")
    P = [int(x) for x in P.split()]

    result = GreedySorting(P)
    for res in result:
        print("(" + " ".join(["+" + str(x) if x > 0 else str(x) for x in res]) + ")")
