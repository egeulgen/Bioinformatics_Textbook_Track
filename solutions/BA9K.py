import sys


def LastToFirst(BWT, i):
    counts = {}
    BWT_list = []
    for char in BWT:
        if char not in counts.keys():
            counts[char] = 1
        else:
            counts[char] += 1
        tmp = char + str(counts[char])
        BWT_list.append(tmp)

    first_col = sorted(BWT_list, key=lambda x: x[0])

    last_to_first = []
    for sym_last in BWT_list:
        for idx, sym_first in enumerate(first_col):
            if sym_first == sym_last:
                last_to_first.append(idx)

    return last_to_first[i]


if __name__ == "__main__":
    '''
    Given: A string Transform and an integer i.
    Return: The position LastToFirst(i) in FirstColumn in the Burrows-Wheeler matrix if LastColumn = Transform.
    '''
    input_lines = sys.stdin.read().splitlines()
    Transform = input_lines[0]
    i = int(input_lines[1])

    print(LastToFirst(Transform, i))
