import sys


def reconstruct_string(pattern):
    string = pattern[0]
    for i in range(1, len(pattern)):
        string += pattern[i][-1]
    return string


if __name__ == "__main__":
    '''
    Given: A sequence of k-mers Pattern1, ... , Patternn such that the last k - 1 symbols of Patterni are equal to the 
    first k - 1 symbols of Patterni+1 for i from 1 to n-1.
    Return: A string Text of length k+n-1 where the i-th k-mer in Text is equal to Patterni for all i.
    '''
    Pattern = sys.stdin.read().splitlines()

    print(reconstruct_string(Pattern))
