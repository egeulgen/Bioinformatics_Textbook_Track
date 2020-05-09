import sys


def positions_pattern(text, pattern):
    k = len(pattern)
    pos = []
    for i in range(len(text) - k + 1):
        if text[i:i+k] == pattern:
            pos.append(i)
    return pos


if __name__ == "__main__":
    '''
    Given: Strings Pattern and Genome.
    Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.
    '''
    input_lines = sys.stdin.read().splitlines()
    Pattern = input_lines[0]
    Genome = input_lines[1]

    print(" ".join(map(str, positions_pattern(Genome, Pattern))))
