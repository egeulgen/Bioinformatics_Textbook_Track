import sys


def PartialSuffixArray(Text, K):
    suffixes = []
    suffix_array = []
    for i in range(len(Text)):
        suffixes.append(Text[i:])
        suffix_array.append(i)

    suffix_array = [x for _, x in sorted(zip(suffixes, suffix_array), key=lambda pair: pair[0])]

    partial_suffix_array = [(i, x) for i, x in enumerate(suffix_array) if x % K == 0]

    return partial_suffix_array


if __name__ == '__main__':
    '''
    Given: A string Text and a positive integer K.
    Return: SuffixArrayK(Text), in the form of a list of ordered pairs (i, SuffixArray(i)) for all nonempty entries in 
    the partial suffix array.
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    K = int(input_lines[1])

    partial_suffix_array = PartialSuffixArray(Text, K)
    for elem in partial_suffix_array:
        print(','.join(map(str, elem)))
