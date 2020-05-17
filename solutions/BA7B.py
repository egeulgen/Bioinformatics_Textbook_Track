import sys


def limb_length(distance_mat, j, n_leaves):
    other_leaves = [i for i in range(n_leaves) if i != j]

    ll = []
    for idx_i in range(len(other_leaves) - 1):
        for idx_k in range(idx_i, len(other_leaves)):
            i = other_leaves[idx_i]
            k = other_leaves[idx_k]
            ll.append((distance_mat[i][j] + distance_mat[j][k] - distance_mat[i][k]) / 2)
    return min(ll)

if __name__ == "__main__":
    '''
    Given: An integer n, followed by an integer j between 0 and n - 1, followed by a space-separated additive distance 
    matrix D (whose elements are integers).
    Return: The limb length of the leaf in Tree(D) corresponding to row j of this distance matrix (use 0-based indexing)
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    j = int(input_lines[1])
    distance_mat = [[int(x) for x in line.split()] for line in input_lines[2:]]

    print(limb_length(distance_mat, j, n))
