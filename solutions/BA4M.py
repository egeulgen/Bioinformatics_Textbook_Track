import sys


def delta(A):
    result = []
    for i in range(len(A)):
        for j in range(len(A)):
            result.append(A[i] - A[j])
    return result


def is_multi_subset(A, B):
    for elem in A:
        if A.count(elem) > B.count(elem):
            return False
    return True


def diffence(A, B):
    # A - B
    diffset = []
    all_elems = list(set(A))
    for elem in all_elems:
        n = A.count(elem) - B.count(elem)
        for _ in range(n):
            diffset.append(elem)
    return diffset


def Place(L):
    while L:
        y = L.pop(-1)

        # place on left
        tmp = delta([y] + X)
        if tmp == L_original:
            res = [y] + X
            res.sort()
            return res

        if is_multi_subset(tmp, L_original):
            X.append(y)
            L_left = diffence(L, tmp)
            res_l = Place(L_left)
            X.remove(y)
            if res_l is not None:
                return res_l

        # place on right
        tmp = delta([width - y] + X)
        if tmp == L_original:
            res = [y] + X
            res.sort()
            return res

        if is_multi_subset(tmp, L_original):
            X.append(width - y)
            L_right = diffence(L, tmp)
            res_r = Place(L_right)
            X.remove(width - y)
            if res_r is not None:
                return res_r
    return X


if __name__ == "__main__":
    '''
    Given: A collection of integers L.
    Return: A set A such that ∆A = L.
    '''
    ## NEED TO FIX THIS
    L = [int(x) for x in sys.stdin.readline().strip().split()]

    L_original = L[:]
    width = L.pop(-1)
    X = [0, width]
    L = [x for x in L if x > 0]

    result = Place(L)

    print(" ".join(map(str, result)))
