import sys
from BA9I import BurrowsWheelerTransform


def create_check_point_array(BWT, C):
    symbol_list = list(set(BWT))
    check_point_array = {}
    for idx in range(0, len(BWT), C):
        check_point_array[idx] = {}
        for symbol in symbol_list:
            check_point_array[idx][symbol] = BWT[:idx].count(symbol)
    return check_point_array


def Count_symbol(check_point_array, idx, LastColumn, symbol):
    vals = [x for x in check_point_array.keys() if x <= idx]
    nearest_idx = min(vals, key=lambda x: abs(x - idx))

    count = check_point_array[nearest_idx][symbol]
    count += LastColumn[nearest_idx:idx].count(symbol)
    return count


def PartialSuffixArray(Text, K):
    suffixes = []
    suffix_array = []
    for i in range(len(Text)):
        suffixes.append(Text[i:])
        suffix_array.append(i)

    suffix_array = [x for _, x in sorted(zip(suffixes, suffix_array), key=lambda pair: pair[0])]

    partial_suffix_array = {i: x for i, x in enumerate(suffix_array) if x % K == 0}

    return partial_suffix_array


def MultiplePatternMatching(FirstOccurrence, LastColumn, pattern, check_point_array):
    ''' Multiple Pattern Matching with BWT
    '''
    top = 0
    bottom = len(LastColumn) - 1

    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            # if positions from top to bottom in LastColumn
            # contain any occurrence of symbol
            if symbol in LastColumn[top: bottom + 1]:
                top = FirstOccurrence[symbol] + Count_symbol(check_point_array, top, LastColumn, symbol)
                bottom = FirstOccurrence[symbol] + Count_symbol(check_point_array, bottom + 1, LastColumn, symbol) - 1
            else:
                return False, False
        else:
            return top, bottom


def wrapper(Text, pattern_list, C):
    BWT = BurrowsWheelerTransform(Text + '$')

    FirstOccurrence = {}
    for idx, symbol in enumerate(sorted(BWT)):
        if symbol not in FirstOccurrence.keys():
            FirstOccurrence[symbol] = idx

    check_point_array = create_check_point_array(BWT, C)
    partial_suffix_array = PartialSuffixArray(Text + '$', C)

    positions_list = []
    for pattern in pattern_list:
        top, bottom = MultiplePatternMatching(FirstOccurrence, BWT, pattern, check_point_array)
        if top:
            for idx in range(top, bottom + 1):

                to_add = 0
                while idx not in partial_suffix_array.keys():
                    idx = FirstOccurrence[BWT[idx]] + Count_symbol(check_point_array, idx, BWT, BWT[idx])
                    to_add += 1

                positions_list.append(partial_suffix_array[idx] + to_add)

    return sorted(positions_list)


if __name__ == "__main__":
    ''' Multiple Patterns Matching Implementation (with BWT)
    Given: A string Text and a collection of strings Patterns.
    Return: All starting positions in Text where a string from Patterns appears as a substring.
    '''
    tmp = sys.stdin.read().splitlines()
    Text = tmp[0]
    pattern_list = []
    for i in range(1, len(tmp)):
        pattern_list.append(tmp[i])

    positions_list = wrapper(Text, pattern_list, C=100)
    print(' '.join(str(pos) for pos in positions_list))
