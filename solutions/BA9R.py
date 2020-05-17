import sys
from Tree_Trie_classes import Tree


if __name__ == "__main__":
    '''
    Given: A string Text, SuffixArray(Text), and LCP(Text).
    Return: The strings labeling the edges of SuffixTree(Text). (You may return these strings in any order.)
    '''
    input_lines = sys.stdin.read().splitlines()
    Text = input_lines[0]

    tree = Tree()
    tree.PopulateSuffixTree(Text)

    result = tree.edge_labels(Text)
    print("\n".join(result))