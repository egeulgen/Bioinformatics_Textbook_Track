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


def difference(A, B):
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
        if delta(X) == L_original:
            X.sort()
            return X

        y = L.pop(-1)

        # place on left
        tmp = delta([y] + X)
        if is_multi_subset(tmp, L_original):
            X.append(y)
            L_left = difference(L, tmp)
            res_left = Place(L_left)
            X.remove(y)
            if delta(res_left) == L_original:
                res_left.sort()
                return res_left

        # place on right
        tmp = delta([width - y] + X)
        if is_multi_subset(tmp, L_original):
            X.append(width - y)
            L_right = difference(L, tmp)
            res_right = Place(L_right)
            X.remove(width - y)
            if delta(res_right) == L_original:
                res_right.sort()
                return res_right
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
