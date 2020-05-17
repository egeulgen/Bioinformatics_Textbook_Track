import sys


def BWMatching_wrapper(BWT, pattern_list):
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

    result = []
    for pattern in pattern_list:
        result.append(BWMatching(BWT, pattern, last_to_first))

    return result


def BWMatching(last_column, pattern, last_to_first):
    top = 0
    bottom = len(last_column) - 1

    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            # if positions from top to bottom in LastColumn
            # contain any occurrence of symbol

            match_positions = []
            for idx in range(top, bottom + 1):
                if last_column[idx] == symbol:
                    match_positions.append(idx)

            if len(match_positions) != 0:
                top = last_to_first[min(match_positions)]
                bottom = last_to_first[max(match_positions)]
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == "__main__":
    '''
    Given: A string BWT(Text), followed by a collection of strings Patterns.
    Return: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member
    of Patterns in Text.
    '''
    input_lines = sys.stdin.read().splitlines()
    BWT = input_lines[0]
    pattern_list = input_lines[1].split()

    match_nums = BWMatching_wrapper(BWT, pattern_list)
    print(' '.join(map(str, match_nums)))