import sys
from BA10H import print_matrices


def BaumWelchResponsibility(x, transition_matrix, emission_matrix, alphabet, all_states):
    ''' Baum Welch Responsibility Matrices
    Returns the node responsibility matrix (Pr(𝜋𝑖=𝑘|𝑥)) and the edge responsibility matrix (Pr(𝜋𝑖=l, 𝜋𝑖+1=k|𝑥))
    '''

    # assume that transitions from the source node and to sink node occur with equal probability
    init_transition_prob = 1
    # init_transition_prob = 1 / len(all_states)

    ## calculate all forward values (αi(k))
    Forward_dict = {}
    for i in range(len(x)):
        for current_state in all_states:
            if current_state not in Forward_dict.keys():
                Forward_dict[current_state] = {}
            # initialize the recurrence
            # (every node in the leftmost column is connected to source)
            if i == 0:
                # Forward[source] is 1
                Forward_dict[current_state][i] = 1 * init_transition_prob * emission_matrix[current_state][x[i]]

            # forward𝑘,𝑖 = ∑all states 𝑙forward𝑙,𝑖−1⋅Weight𝑖(𝑙,𝑘)
            else:
                Forward_dict[current_state][i] = 0
                for state in all_states:
                    Forward_dict[current_state][i] += Forward_dict[state][i - 1] * transition_matrix[state][
                        current_state] * emission_matrix[current_state][x[i]]
    # Calculate Pr(x)
    Pr_x = 0
    for state in all_states:
        Pr_x += Forward_dict[state][len(x) - 1]

    ## calculate all backward values (βi(k))
    Backward_dict = {}
    for i in range(len(x) - 1, -1, -1):
        for current_state in all_states:
            if current_state not in Backward_dict.keys():
                Backward_dict[current_state] = {}

            # initialize the recurrence
            # (every node in the rightmost column is connected to sink)
            if i == len(x) - 1:
                Backward_dict[current_state][i] = 1
            # backward𝑘,𝑖 = ∑all states 𝑙backward𝑙,𝑖+1⋅Weight𝑖(𝑙,𝑘)
            else:
                Backward_dict[current_state][i] = 0
                for state in all_states:
                    Backward_dict[current_state][i] += Backward_dict[state][i + 1] * transition_matrix[current_state][
                        state] * emission_matrix[state][x[i + 1]]

    ## Create Node Responsibility Matrix containing Pr(𝜋𝑖=𝑘|𝑥) = ( αi(k) * βi(k) / α(sink) ) for each position i, each state k given emitted string x
    node_responsibility_matrix = {}
    for i in range(len(x)):
        for state in all_states:
            node_responsibility_matrix[(state, i)] = Forward_dict[state][i] * Backward_dict[state][i] / Pr_x

    ## Create Edge Responsibility Matrix containing Pr(𝜋𝑖=l, 𝜋𝑖+1=k|𝑥) = αi(l) * weight i(l,k) * βi+1(k) / α(sink) (i.e. the denominator is Pr_x)
    # for each position i, each pair of states k, l given emitted string x

    edge_responsibility_matrix = {}
    for i in range(len(x) - 1):
        for state1 in all_states:
            for state2 in all_states:
                if (state1, state2) not in edge_responsibility_matrix.keys():
                    edge_responsibility_matrix[(state1, state2)] = {}

                edge_responsibility_matrix[(state1, state2)][i] = Forward_dict[state1][i] * transition_matrix[state1][
                    state2] * emission_matrix[state2][x[i + 1]] * Backward_dict[state2][i + 1] / Pr_x

    return [node_responsibility_matrix, edge_responsibility_matrix]


def BaumWelchParameterEstimation(x, responsibility_profile, alphabet, all_states):
    node_responsibility_matrix, edge_responsibility_matrix = responsibility_profile
    transition_matrix = {}
    emission_matrix = {}

    ## Transition(k, l) = SUMi=1, n - 1 edge_responsibility_matrix[(k,l)][i]
    for state1 in all_states:
        transition_matrix[state1] = {}
        transition = {}
        for state2 in all_states:
            transition[state2] = 0
            for i in range(len(x) - 1):
                transition[state2] += edge_responsibility_matrix[(state1, state2)][i]
            norm_factor = sum(transition.values())
        for state2 in all_states:
            transition_matrix[state1][state2] = transition[state2] / norm_factor

    ## Emission(k, symbol) = SUMi=1, n Pr(𝜋𝑖=𝑘|𝑥) if xi = symbol and 0 otherwise
    for state in all_states:
        emission_matrix[state] = {}
        emission = {}
        for symbol in alphabet:
            emission[symbol] = 0
            for i in range(len(x)):
                emission[symbol] += (node_responsibility_matrix[(state, i)] if x[i] == symbol else 0)
            norm_factor = sum(emission.values())
        for symbol in alphabet:
            emission_matrix[state][symbol] = emission[symbol] / norm_factor

    return transition_matrix, emission_matrix


def BaumWelchLearning(x, init_transition_matrix, init_emission_matrix, alphabet, all_states, max_iterations):
    transition_matrix = init_transition_matrix
    emission_matrix = init_emission_matrix

    for iteration in range(max_iterations):
        # Step 1: (E-Step) re-estimate the responsibility profile given the current HMM parameters
        responsibility_profile = BaumWelchResponsibility(x, transition_matrix, emission_matrix, alphabet, all_states)

        # Step 2: (M-Step) re-estimate the HMM parameters given the current responsibility profile
        transition_matrix, emission_matrix = BaumWelchParameterEstimation(x, responsibility_profile, alphabet,
                                                                          all_states)

    return transition_matrix, emission_matrix


if __name__ == "__main__":
    '''
    Given: A sequence of emitted symbols x = x1 . . . xn in an alphabet A, generated by a k-state HMM with unknown 
    transition and emission probabilities, initial Transition and Emission matrices and a number of iterations I.
    Return: A matrix of transition probabilities Transition and a matrix of emission probabilities Emission that 
    maximizes Pr(x,π) over all possible transition and emission matrices and over all hidden paths π.
    '''
    tmp = sys.stdin.read().splitlines()

    max_iterations = int(tmp[0])
    x = tmp[2]
    alphabet = tmp[4].split()
    all_states = tmp[6].split()

    init_transition_matrix = {}
    init_emission_matrix = {}

    # initial transition matrix
    col_syms = tmp[8].split('\t')[1:]
    transition_end = 8 + len(all_states)

    for i in range(9, transition_end + 1):
        current_line = tmp[i].rstrip().split('\t')
        row_sym = current_line[0]
        init_transition_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            init_transition_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    # emission matrix
    col_syms = tmp[transition_end + 2].split('\t')[1:]

    for i in range(transition_end + 3, len(tmp)):
        current_line = tmp[i].rstrip().split('\t')
        row_sym = current_line[0]
        init_emission_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            init_emission_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    transition_matrix, emission_matrix = BaumWelchLearning(x, init_transition_matrix, init_emission_matrix, alphabet,
                                                           all_states, max_iterations)

    print_matrices(transition_matrix, emission_matrix)
