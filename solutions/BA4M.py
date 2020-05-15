import sys


def delta2(S, T):
    A = list(S)
    B = list(T)
    result = []
    for a in A:
        for b in B:
                result.append(abs(a - b))
    return result


def is_multi_subset(A, B):
    for elem in A:
        if A.count(elem) > B.count(elem):
            return False
    return True


def difference(A, B):
    # A - B
    diffset = []
    all_elems = set(A)
    for elem in all_elems:
        n = A.count(elem) - B.count(elem)
        if n > 0:
            for _ in range(n):
                diffset.append(elem)
    diffset.sort()
    return diffset


def Place(dist_l):
    if not dist_l:
        return X

    y = dist_l[-1]
    # place on left
    tmp = delta2({y}, X)
    if is_multi_subset(tmp, dist_l):
        X.add(y)
        L_left = difference(dist_l, tmp)
        res_left = Place(L_left)
        if res_left:
            return res_left
        X.remove(y)

    # place on right
    tmp = delta2({width - y}, X)
    if is_multi_subset(tmp, dist_l):
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
    # Zhang Z. An exponential example for a partial digest mapping algorithm. J Comput Biol. 1994;1(3):235-9.
    L = [int(x) for x in sys.stdin.readline().strip().split()]
    L = [x for x in L if x > 0]

    width = L.pop(-1)
    X = {0, width}

    result = Place(L)

    print(" ".join(map(str, result)))
