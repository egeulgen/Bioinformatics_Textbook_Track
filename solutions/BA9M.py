import sys


def BetterBWMatching_wrapper(BWT, pattern_list):
    FirstOccurrence = {}
    for idx, symbol in enumerate(sorted(BWT)):
        if symbol not in FirstOccurrence.keys():
            FirstOccurrence[symbol] = idx

    result = []
    for pattern in pattern_list:
        result.append(BetterBWMatching(FirstOccurrence, BWT, pattern))

    return result


def Countsymbol(idx, LastColumn, symbol):
    return LastColumn[:idx].count(symbol)


def BetterBWMatching(FirstOccurrence, LastColumn, pattern):
    ''' Better Burrows Wheeler Matching
    BetterBWMatching(FirstOccurrence, LastColumn, Pattern)
        top ← 0
        bottom ← |LastColumn| − 1
        while top ≤ bottom
            if Pattern is nonempty
                symbol ← last letter in Pattern
                remove last letter from Pattern
                if positions from top to bottom in LastColumn contain an occurrence of symbol
                    top ← FirstOccurrence(symbol) + Countsymbol(top, LastColumn)
                    bottom ← FirstOccurrence(symbol) + Countsymbol(bottom + 1, LastColumn) − 1
                else
                    return 0
            else
                return bottom − top + 1
    '''
    top = 0
    bottom = len(LastColumn) - 1

    while top <= bottom:
        if len(pattern) != 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            # if positions from top to bottom in LastColumn
            # contain any occurrence of symbol
            if symbol in LastColumn[top:bottom + 1]:
                top = FirstOccurrence[symbol] + Countsymbol(top, LastColumn, symbol)
                bottom = FirstOccurrence[symbol] + Countsymbol(bottom + 1, LastColumn, symbol) - 1
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
    tmp = sys.stdin.read().splitlines()
    BWT = tmp[0]
    pattern_list = tmp[1].split(' ')

    match_nums = BetterBWMatching_wrapper(BWT, pattern_list)
    print(' '.join(str(num) for num in match_nums))
