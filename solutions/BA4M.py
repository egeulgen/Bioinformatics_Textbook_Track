import sys


def delta(S):
    A = list(S)
    result = []
    for i in range(len(A)):
        for j in range(len(A)):
            result.append(A[i] - A[j])
    result.sort()
    return result


def is_multi_subset(A, B):
    for elem in A:
        if A.count(elem) > B.count(elem):
            return False
    return True


def difference(A, B):
    # A - B
    diffset = []
    all_elems = (A)
    for elem in all_elems:
        n = A.count(elem) - B.count(elem)
        for _ in range(n):
            diffset.append(elem)
    diffset.sort()
    return diffset


def Place(dist_l):
    if len(dist_l) == 0:
        return X

    y = dist_l.pop(-1)

    # place on left
    tmp = delta({y} | X)
    if is_multi_subset(tmp, L_original):
        X.add(y)
        L_left = difference(dist_l, tmp)
        res_left = Place(L_left)
        if res_left:
            return res_left
        X.remove(y)

    # place on right
    tmp = delta({width - y} | X)
    if is_multi_subset(tmp, L_original):
        X.add(width - y)
        L_right = difference(dist_l, tmp)
        res_right = Place(L_right)
        if res_right:
            return res_right
        X.remove(width - y)
    return {}


if __name__ == "__main__":
    '''
    Given: A collection of integers L.
    Return: A set A such that ∆A = L.
    '''
    ## NEED TO FIX THIS
    L = [int(x) for x in sys.stdin.readline().strip().split()]

    L_original = L[:]
    width = L.pop(-1)
    X = {0, width}
    L = list(set([x for x in L if x > 0]))

    result = Place(L)

    print(" ".join(map(str, result)))

    print("\n\n")
    # print(L_original)
    d = delta(result)
    d.sort()
    # print(d)
    print(d == L_original)
