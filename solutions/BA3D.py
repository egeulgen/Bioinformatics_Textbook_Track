import sys
from collections import OrderedDict


def deBruijn_graph(text, k):
    adj_list = OrderedDict()
    for i in range(len(text) - k + 2):
        adj_list[text[i:i + k - 1]] = set()

    for i in range(len(text) - k + 1):
        pattern = text[i:i + k - 1]
        pattern2 = text[i + 1:i + k]
        adj_list[pattern].add(pattern2)

    return adj_list


if __name__ == "__main__":
    '''
    Given: An integer k and a string Text.
    Return:DeBruijnk(Text), in the form of an adjacency list.
    '''
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])
    Text = input_lines[1]

    adj_list = deBruijn_graph(Text, k)
    for key, val in adj_list.items():
        if val:
            print(key + ' -> ' + ",".join(val))
