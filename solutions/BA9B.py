import sys
from BA9A import TrieConstruction


def PrefixTrieMatching(Prefix, trie):
    ''' Prefix Trie Matching
    '''
    symbol = Prefix[0]
    node = trie.root

    idx = 1
    pattern = ''

    while True:
        # if node is a leaf
        if len(node.edges) == 0:
            return pattern

        # if there is an edge (node, some other node) in Trie,
        # labeled by symbol, extend pattern
        found = False
        for edge in node.edges:
            if edge.label == symbol:
                found = True
                pattern += symbol
                node = edge.target_node
                if idx != len(Prefix):
                    symbol = Prefix[idx]
                    idx += 1
                break

        if not found:
            return None


def TrieMatching(Text, trie):
    indices = []
    idx = 0
    while len(Text) != 0:
        match = PrefixTrieMatching(Text, trie)
        if match != None:
            indices.append(idx)
        Text = Text[1:]
        idx += 1
    return indices


if __name__ == "__main__":
    '''
    Given: A string Text and a collection of strings Patterns.
    Return: All starting positions in Text where a string from Patterns appears as a substring.
    '''
    tmp = sys.stdin.read().splitlines()
    Text = tmp[0]
    Patterns = []
    for i in range(1, len(tmp)):
        Patterns.append(tmp[i])

    trie = TrieConstruction(Patterns)
    result = TrieMatching(Text, trie)
    print(' '.join(str(x) for x in result))