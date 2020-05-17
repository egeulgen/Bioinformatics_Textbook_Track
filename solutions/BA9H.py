import sys


def pattern_matching(Text, Patterns):
    # how to do this with suffix array?
    match_idx = []
    for pattern in Patterns:
        for j in range(len(Text) - len(pattern) + 1):
            if pattern == Text[j:j + len(pattern)]:
                match_idx.append(j)
    match_idx = sorted(match_idx)
    return match_idx


if __name__ == "__main__":
    '''
    Given: A string Text and a collection of strings Patterns.
    Return: All starting positions in Text where a string from Patterns appears as a substring.
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    Patterns = input_lines[1:]

    print(" ".join(map(str, pattern_matching(Text, Patterns))))
