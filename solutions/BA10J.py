import sys


def SoftDecoding(x, transition_matrix, emission_matrix, alphabet, all_states):
    # assume that transitions from the source node and to sink node occur with equal probability
    init_transition_prob = 1 / len(all_states)

    ## calculate all forward values
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

    Pr_x = 0
    for state in all_states:
        Pr_x += Forward_dict[state][len(x) - 1]

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

    cond_prob_matrix = {}
    for i in range(len(x)):
        for state in all_states:
            if state not in cond_prob_matrix.keys():
                cond_prob_matrix[state] = {}

            cond_prob_matrix[state][i] = Forward_dict[state][i] * Backward_dict[state][i] / Pr_x

    return cond_prob_matrix


if __name__ == "__main__":
    '''
    Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, 
    transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
    Return: The probability Pr(πi = k|x) that the HMM was in state k at step i (for each state k and each step i).
    '''
    tmp = sys.stdin.read().splitlines()

    x = tmp[0]
    alphabet = tmp[2].split()
    all_states = tmp[4].split()

    transition_matrix = {}
    emission_matrix = {}

    # initial transition matrix
    col_syms = tmp[6].split()
    transition_end = 6 + len(all_states)

    for i in range(7, transition_end + 1):
        current_line = tmp[i].split()
        row_sym = current_line[0]
        transition_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            transition_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    # emission matrix
    col_syms = tmp[transition_end + 2].split()

    for i in range(transition_end + 3, len(tmp)):
        current_line = tmp[i].split()
        row_sym = current_line[0]
        emission_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            emission_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    cond_prob_matrix = SoftDecoding(x, transition_matrix, emission_matrix, alphabet, all_states)

    to_print = '\t'.join(all_states) + '\n'
    for i in range(len(x)):
        for state in all_states:
            to_print += str(round(cond_prob_matrix[state][i], 4)).rstrip('0') + '\t'
        to_print += '\n'

    print(to_print)
