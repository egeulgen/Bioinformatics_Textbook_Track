import sys


def composition(text, k):
    for i in range(len(text) - k + 1):
        yield text[i:i + k]


if __name__ == "__main__":
    '''
    Given: An integer k and a string Text.
    Return: Compositionk(Text) (the k-mers can be provided in any order).
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])
    Text = input_lines[1]

    for kmer in composition(Text, k):
        print(kmer)
