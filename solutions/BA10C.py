import sys


def Viterbi(x, all_states, transition_matrix, emission_matrix):
    init_transition_prob = 1 / len(all_states)

    ## calculate all scores
    backtrace = {}
    Score_dict = {}
    for i in range(len(x)):
        backtrace[i] = {}
        for current_state in all_states:
            if current_state not in Score_dict.keys():
                Score_dict[current_state] = {}
            ## if the leftmost column, initialize the recurrence
            # (every node in the leftmost column is connected to source)
            if i == 0:
                # Score[source] is 1
                Score_dict[current_state][i] = 1 * init_transition_prob * emission_matrix[current_state][x[i]]
                # print(str(i) + ': '+ 'source' + '>>' + current_state + ':\t' + '{:.5f}'.format(init_transition_prob * emission_matrix[current_state][x[i]]))

            # 𝑠𝑘,𝑖 = max𝑎𝑙𝑙 𝑠𝑡𝑎𝑡𝑒𝑠 𝑙{𝑠𝑙,𝑖−1⋅𝑡𝑟𝑎𝑛𝑠𝑖𝑡𝑖𝑜𝑛𝑙,𝑘⋅𝑒𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑘(𝑥𝑖)}
            else:
                Score_dict[current_state][i] = -1e6
                for state in all_states:
                    tmp_score = Score_dict[state][i - 1] * transition_matrix[state][current_state] * \
                                emission_matrix[current_state][x[i]]
                    # print(str(i) + ': '+ state + '>>' + current_state + ':\t' + '{:.5f}'.format(transition_matrix[state][current_state] * emission_matrix[current_state][x[i]]))
                    if tmp_score > Score_dict[current_state][i]:
                        Score_dict[current_state][i] = tmp_score
                        backtrace[i][current_state] = state

    ## Backtrace the maximum scoring path
    max_score_state = max(Score_dict.keys(), key=lambda state: Score_dict[state][len(x) - 1])
    most_probable_path = max_score_state

    current_state = max_score_state
    for i in range(len(x) - 1, 0, -1):
        prev_state = backtrace[i][current_state]
        most_probable_path = prev_state + most_probable_path
        current_state = prev_state

    # print('\t' + '\t'.join([str(i) for i in range(len(x))]))
    # to_print = ''
    # for state in all_states:
    #     to_print += state + '\t'
    #     for i in range(len(x)):
    #         to_print += '{:.5f}'.format(Score_dict[state][i]) + '\t'
    #     to_print += '\n'
    # print(to_print)

    return most_probable_path


if __name__ == "__main__":
    '''
    Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, 
    transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
    Return: A path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π.
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
        current_line = tmp[i].split()
        row_sym = current_line[0]
        emission_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            emission_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    print(Viterbi(x, states, transition_matrix, emission_matrix))