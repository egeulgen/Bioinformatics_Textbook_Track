import sys


def ProbabilityOutcomeGivenPath(x, hidden_path, emission_matrix):
    emission_prob = 1
    # Calculate ∏ (i: 1 -> n) emission𝜋𝑖(𝑥𝑖)
    for i in range(len(x)):
        emission_prob *= emission_matrix[hidden_path[i]][x[i]]
    return emission_prob


if __name__ == "__main__":
    '''
    Given: A string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by
    the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission).
    Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π.
    '''
    input_lines = sys.stdin.read().splitlines()

    x = input_lines[0]
    alphabet = input_lines[2].split(' ')
    hidden_path = input_lines[4]

    col_syms = input_lines[8].split()
    emission_matrix = {}
    for line in input_lines[9:]:
        current_line = line.split()
        row_sym = current_line[0]
        emission_matrix[row_sym] = {}
        for j in range(1, len(current_line)):
            emission_matrix[row_sym][col_syms[j - 1]] = float(current_line[j])

    print(ProbabilityOutcomeGivenPath(x, hidden_path, emission_matrix))