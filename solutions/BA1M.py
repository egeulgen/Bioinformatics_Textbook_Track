import sys


def NumberToPattern(Number, k):
    reverse = ['A', 'C', 'G', 'T']
    Pattern = ''
    for i in range(k - 1, -1, -1):
        current = Number // 4 ** i
        Pattern += reverse[current]
        Number %= 4 ** i
    return Pattern


if __name__ == "__main__":
    '''
    Given: Integers index and k.
    Return: NumberToPattern(index, k).
    '''
    input_lines = sys.stdin.read().splitlines()
    index = int(input_lines[0])
    k = int(input_lines[1])

    print(NumberToPattern(index, k))