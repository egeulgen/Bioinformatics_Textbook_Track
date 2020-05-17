import sys


def SuffixArray(Text):
    suffixes = []
    suffix_array = []
    for i in range(len(Text)):
        suffixes.append(Text[i:])
        suffix_array.append(i)

    suffix_array = [x for _, x in sorted(zip(suffixes, suffix_array), key=lambda pair: pair[0])]

    return suffix_array


if __name__ == "__main__":
    '''
    Input: A string Text.
    Output: SuffixArray(Text).
    '''
    Text = sys.stdin.read().rstrip()
    suffix_array = SuffixArray(Text)

    print(', '.join(str(x) for x in suffix_array))