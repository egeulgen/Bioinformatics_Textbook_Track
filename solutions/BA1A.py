import sys


def count_pattern(text, pattern):
    k = len(pattern)
    count = 0
    for i in range(len(text) - k + 1):
        if text[i:i+k] == pattern:
            count += 1
    return count


if __name__ == "__main__":
    '''
    Given: {DNA strings}} Text and Pattern.
    Return: Count(Text, Pattern).
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]
    Pattern = input_lines[1]
    print(count_pattern(Text, Pattern))