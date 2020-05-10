import sys


def PatternToNumber(Pattern):
    indices = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    result = 0
    N = len(Pattern)
    for i in range(N):
        nuc = Pattern[i]
        result += indices[nuc] * 4 ** (N - i - 1)
    return result


if __name__ == "__main__":
    '''
    Given: A DNA string Pattern.
    Return: PatternToNumber(Pattern).
    '''
    input_lines = sys.stdin.read().splitlines()
    Pattern = input_lines[0]

    print(PatternToNumber(Pattern))