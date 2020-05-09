import sys


def hamming_dist(string1, string2):
    return sum([x != y for x, y in zip(string1, string2)])


if __name__ == "__main__":
    '''
    Given: Two DNA strings.
    Return: An integer value representing the Hamming distance.
    '''
    input_lines = sys.stdin.read().splitlines()
    dna1 = input_lines[0]
    dna2 = input_lines[1]

    print(hamming_dist(dna1, dna2))
