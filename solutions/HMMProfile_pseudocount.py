import sys

def is_transition_valid(state1, state2, end_idx):
    ''' Is Transition Valid (Non-forbidden)
    Function to determine if the transition 
    from state1 to state2 is present in the
    HMM Profile Graph
    '''

    def parse_state(state):
        '''
        Function to parse each state (type and index)
        '''
        s_type = state.rstrip('0123456789')
        s_idx = state[len(s_type):]
        if s_type == 'S':
            s_idx = 0
        return s_type, int(s_idx) if s_idx != '' else -1

    state1, state2 = [parse_state(s) for s in (state1, state2)]

    # valid transitions to end state
    if state2[0] == 'E':
        if state1[0] + str(state1[1]) in [s + str(end_idx) for s in ['M', 'I', 'D']]:
            return True

    # other valid transitions
    if state1[0] != 'E':
        if state2[0] + str(state2[1]) in ['D' + str(state1[1] + 1), 'M' + str(state1[1] + 1), 'I' + str(state1[1])]:
            return True

    return False
    
def print_matrices(*argv, delim = "\t", separator = "--------"):
    ''' Function for printing multiple matrices
    Prints each matrix (stored as a dictionary) in 
    tab-delimited format (default). Seperates the 
    matrices with '--------' (default).
    '''

    for idx, matrix in enumerate(argv):

        row_labels = list(matrix.keys())
        col_labels = list(matrix[row_labels[0]].keys())
        if idx == 0:
            to_print = delim + delim.join(col_labels) + '\n'
            # to_print = delim + delim.join(col_labels) + '\t\n' # fix for required format
        else:
            to_print = delim + delim.join(col_labels) + '\n'

        for r_label in row_labels:
            tmp = [r_label]
            for c_label in col_labels:
                val = matrix[r_label][c_label]
                if val == 0:
                    val_str = '0'
                elif val == int(val):
                    val_str = '{:.1f}'.format(val)
                else:
                    val_str = '{:.3f}'.format(val).rstrip('0')
                tmp.append(val_str)
            to_print += delim.join(tmp)
            if r_label != row_labels[-1]:
                to_print += '\n'

        print(to_print)
        if idx != len(argv) - 1:
            print(separator)

    return None

def ProfileHMM(alignment, alphabet, insertion_threshold, pseudocount):
    ''' The Profile HMM with Pseudocounts Problem
    Input: A threshold θ and a pseudocount σ, followed by an alphabet Σ, followed by a
     multiple alignment Alignment whose strings are formed from Σ.
    Output: The transition and emission matrices of HMM(Alignment, θ, σ).

    Note: Your matrices can be either space-separated or tab-separated.
    '''

    ##### Remove columns if the fraction of insertion exceeds he maximum fraction of insertions per column
    cols_to_keep = []
    num_cols = len(alignment[0])
    for j in range(num_cols):
        col = []
        for i in range(len(alignment)):
            col.append(alignment[i][j])
        if sum(x == '-' for x in col) / len(col) < insertion_threshold:
            cols_to_keep.append(j)

    ##### Determine all possible states
    all_states = ['S', 'I0']
    for i in range(len(cols_to_keep)):
        all_states.append('M' + str(i + 1))
        all_states.append('D' + str(i + 1))
        all_states.append('I' + str(i + 1))
    all_states.append('E')

    ##### Calculate transition probabilities using the sequences in alignment
    # initialize transitions numbers matrix
    num_transitions = {}
    for state1 in all_states:
        num_transitions[state1] = {}
        for state2 in all_states:
            num_transitions[state1][state2] = 0

    for current_seq in alignment:
        current_state = 'S'
        col_idx = 0

        while current_state != 'E':

            # determine state index
            if current_state == 'S':
                current_state_idx = 0
            else:
                current_state_idx = int(''.join(x for x in current_state if x.isdigit()))

            ## Determine next state
            # end state
            if col_idx == len(current_seq):
                next_state = 'E'

            elif col_idx in cols_to_keep:
                # match
                if current_seq[col_idx] != '-':
                    next_state = 'M' + str(current_state_idx + 1)
                # deletion
                else:
                    next_state = 'D' + str(current_state_idx + 1)
            # insertion
            elif col_idx not in cols_to_keep and current_seq[col_idx] != '-':
                next_state = 'I' + str(current_state_idx)
            
            # to pass deletion in non-included column
            if next_state != current_state or (current_state.startswith('I') and current_seq[col_idx] != '-'):
                num_transitions[current_state][next_state] += 1
                current_state = next_state

            col_idx += 1

    # turn number of transitions matrix to transition matrix
    raw_transition_matrix = {}
    for state1, row in num_transitions.items():
        row_total = sum(row.values())
        raw_transition_matrix[state1] = {}
        for state2, val in row.items():
            if row_total != 0:
                raw_transition_matrix[state1][state2] = val / row_total
            else:
                raw_transition_matrix[state1][state2] = val

    # adding the pseudocount and renormalizing to get the final transition matrix
    transition_matrix = {}
    end_idx = len(cols_to_keep)
    for state1, row in raw_transition_matrix.items():
        transition_matrix[state1] = {}

        # calculate normalization factor
        norm_factor = 0
        for state2 in all_states:
            if is_transition_valid(state1, state2, end_idx):
                norm_factor += row[state2] + pseudocount

        # add pseudocount to value and normalize
        for state2, val in row.items():
            if is_transition_valid(state1, state2, end_idx):
                transition_matrix[state1][state2] = (val + pseudocount) / norm_factor
            else:
                transition_matrix[state1][state2] = val
    
    ##### Calculate emission probabilities using the sequences in alignment
    # initialize emission numbers matrix
    num_emissions = {}
    for state in all_states:
        num_emissions[state] = {}
        for symbol in alphabet:
            num_emissions[state][symbol] = 0
            
    for current_seq in alignment:
        current_state = 'S'
        col_idx = 0

        while current_state != 'E':

            # determine state index
            if current_state == 'S':
                current_state_idx = 0
            else:
                current_state_idx = int(''.join(x for x in current_state if x.isdigit()))

            ## Determine next state
            if col_idx == len(current_seq):
                next_state = 'E'
            
            elif col_idx in cols_to_keep:
                # match
                if current_seq[col_idx] != '-':
                    next_state = 'M' + str(current_state_idx + 1)
                # deletion
                else:
                    next_state = 'D' + str(current_state_idx + 1)
            # insertion
            elif col_idx not in cols_to_keep and current_seq[col_idx] != '-':
                next_state = 'I' + str(current_state_idx)
            
            # to pass deletion in non-included column
            if next_state != 'E':
                sym = current_seq[col_idx]
                if next_state != current_state or (current_state.startswith('I') and sym != '-'):
                    if sym != '-':
                        num_emissions[next_state][sym] += 1
            current_state = next_state
            col_idx += 1

    # turn number of emissions matrix to emission matrix
    raw_emission_matrix = {}
    for state, row in num_emissions.items():
        row_total = sum(row.values())
        raw_emission_matrix[state] = {}
        for symbol, val in row.items():
            if row_total != 0:
                raw_emission_matrix[state][symbol] = val / row_total
            else:
                raw_emission_matrix[state][symbol] = val

    # adding the pseudocount and renormalizing to get the final emission matrix
    emission_matrix = {}
    end_idx = len(cols_to_keep)
    for state, row in raw_emission_matrix.items():
        emission_matrix[state] = {}

        if state != 'S' and state != 'E' and not state.startswith('D'):
            # calculate normalization factor
            norm_factor = 0
            for val in row.values():
                norm_factor += val + pseudocount

            # add pseudocount to value and normalize
            for symbol, val in row.items():
                emission_matrix[state][symbol] = (val + pseudocount) / norm_factor
        else:
            for symbol, val in row.items():
                emission_matrix[state][symbol] = val
    
    return transition_matrix, emission_matrix

if __name__ == "__main__":

    tmp = sys.stdin.read().splitlines()

    insertion_threshold, pseudocount = [float(x) for x in tmp[0].split()] # the insertion fraction threshold and pseudocount
    alphabet = tmp[2].split() # the alphabet that forms the strings in alignment
    
    # alignment 
    alignment = []
    for i in range(4, len(tmp)):
        alignment.append(tmp[i])

    transition_matrix, emission_matrix = ProfileHMM(alignment, alphabet, insertion_threshold, pseudocount)

    print_matrices(transition_matrix, emission_matrix)
