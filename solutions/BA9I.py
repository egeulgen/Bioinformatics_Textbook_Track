import sys


def BurrowsWheelerTransform(Text):
    n = len(Text)
    rotations = sorted([Text[i:] + Text[:i] for i in range(n)])
    bwt = ''.join([rot[-1] for rot in rotations])
    return bwt


if __name__ == "__main__":
    '''
    Given: A string Text.
    Return: BWT(Text).
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]

    print(BurrowsWheelerTransform(Text))
