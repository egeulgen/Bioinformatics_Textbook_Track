import sys
from BA1G import hamming_dist

def positions_approx_pattern(text, pattern, d):
    k = len(pattern)
    pos = []
    for i in range(len(text) - k + 1):
        if hamming_dist(text[i:i+k], pattern) <= d:
            pos.append(i)
    return pos


if __name__ == "__main__":
    '''
    Given: Strings Pattern and Text along with an integer d.
    Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
    '''
    input_lines = sys.stdin.read().splitlines()
    Pattern = input_lines[0]
    Genome = input_lines[1]
    d = int(input_lines[2])

    print(" ".join(map(str, positions_approx_pattern(Genome, Pattern, d))))
