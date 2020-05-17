import sys
from Tree_Trie_classes import Tree


def backtrace_path_from_node(tree, node):
    # if root is reached, stop
    if node.label == 0:
        return ''

    for edge in tree.all_edges:
        if edge.target_node == node:
            incoming_edge = edge
            break

    path_substring = Text[incoming_edge.position: incoming_edge.position + incoming_edge.length]
    path_substring = backtrace_path_from_node(tree, incoming_edge.from_node) + path_substring

    return path_substring


def LongestRepeat(Text):
    suffix_tree = Tree()
    suffix_tree.PopulateSuffixTree(Text + '$')

    ## Find deepest internal node
    max_dep = -1
    for node in suffix_tree.all_nodes:
        if len(node.edges) != 0 and node.depth > max_dep:
            max_dep = node.depth
            max_dep_node = node

    longest_substring = backtrace_path_from_node(suffix_tree, max_dep_node)
    return longest_substring


if __name__ == "__main__":
    '''
    Given: A string Text.
    Return: A longest substring of Text that appears in Text more than once. (Multiple solutions may exist, in which 
    case you may return any one.)
    '''
    Text = sys.stdin.read().rstrip()
    print(LongestRepeat(Text))