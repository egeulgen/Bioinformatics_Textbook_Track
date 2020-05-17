import sys


def OutcomeLikelihood(x, all_states, transition_matrix, emission_matrix):
    init_transition_prob = 1 / len(all_states)

    ## calculate all scores
    Forward_dict = {}
    for i in range(len(x)):
        for current_state in all_states:
            if current_state not in Forward_dict.keys():
                Forward_dict[current_state] = {}
            ## if the leftmost column, initialize the recurrence
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

    outcome_probability = 0
    for state in all_states:
        outcome_probability += Forward_dict[state][len(x) - 1]

    return outcome_probability


if __name__ == "__main__":
    '''
    Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, 
    transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
    Return: The probability Pr(x) that the HMM emits x.
    '''
    tmp = sys.stdin.read().splitlines()

    x = tmp[0]  # the emitted string
    alphabet = tmp[2].split()  # the alphabet from which x was constructed
    states = tmp[4].split()  # the states of HMM

    # transition matrix
    col_syms = tmp[6].split()
    transition_end = 6 + len(states)

    transition_matrix = {}
    for i in range(7, transition_end + 1):
        current_line = tmp[i].split()
        row_sym = current_line[0]
        transition_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            transition_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    # emission matrix
    col_syms = tmp[transition_end + 2].split()
    emission_matrix = {}
    for i in range(transition_end + 3, len(tmp)):
        current_line = tmp[i].rstrip().split()
        row_sym = current_line[0]
        emission_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            emission_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])
    print("{:.11E}".format(OutcomeLikelihood(x, states, transition_matrix, emission_matrix)))