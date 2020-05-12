import sys
from BA3J import StringSpelledByGappedPatterns


if __name__ == "__main__":
    '''
    Given: A sequence of (k, d)-mers (a1|b1), ... , (an|bn) such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for all i 
    from 1 to n-1.
    Return: A string Text where the i-th k-mer in Text is equal to Suffix(ai|bi) for all i from 1 to n, if such a 
    string exists.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, d = [int(x) for x in input_lines[0].split()]
    Gapped_Patterns = []
    for line in input_lines[1:]:
        Gapped_Patterns.append(line.split("|"))

    print(StringSpelledByGappedPatterns(Gapped_Patterns, k - 1, d))
