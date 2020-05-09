import sys

def HiddenPathProbability(hidden_path, transition_matrix):
    ''' Probability of a Hidden Path Problem
    Input: A hidden path π followed by the states States and transition matrix Transition 
    of an HMM (Σ, States, Transition, Emission).
    Output: The probability of this path, Pr(π).

    Note: You may assume that transitions from the initial state occur with equal probability.
    '''

    # initial probability
    prob_path = .5

    # Calculate ∏ (i: 1 -> n) transition𝜋𝑖−1,𝜋𝑖
    for idx in range(1, len(hidden_path)):
        prob_path *= transition_matrix[hidden_path[idx - 1]][hidden_path[idx]]

    return prob_path

if __name__ == "__main__":

    tmp = sys.stdin.read().splitlines()

    hidden_path = tmp[0]
    states = tmp[2].split(' ')
    
    col_syms = tmp[4].split('\t')[1:]
    transition_matrix = {}
    for i in range(5, len(tmp)):
        current_line = tmp[i].rstrip().split('\t')
        row_sym = current_line[0]
        transition_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            transition_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    print(HiddenPathProbability(hidden_path, transition_matrix))