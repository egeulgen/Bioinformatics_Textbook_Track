import sys
from Tree_Trie_classes import Tree


def backtrace_path_from_node(tree, node, Text):
    # if root is reached, stop
    if node.label == 0:
        return ''

    for edge in tree.all_edges:
        if edge.target_node == node:
            incoming_edge = edge
            break

    path_substring = Text[incoming_edge.position: incoming_edge.position + incoming_edge.length]
    path_substring = backtrace_path_from_node(tree, incoming_edge.from_node, Text) + path_substring
    return path_substring


def Shortest_NonShared_Substring(Text1, Text2):
    suffix_tree = Tree()
    combined_Text = Text1 + '#' + Text2 + '$'
    suffix_tree.PopulateSuffixTree(combined_Text)
    suffix_tree.add_indicators()

    ## Find shallowest Text1 internal node
    min_dep = 1e6
    for node in suffix_tree.all_nodes:

        if node.indicator == '#':
            if len(node.edges) != 0 and node.depth <= min_dep:
                min_dep = node.depth
                min_dep_node = node

    non_shared_substr = backtrace_path_from_node(suffix_tree, min_dep_node, combined_Text)
    return non_shared_substr


if __name__ == "__main__":
    '''
    Given: Strings Text1 and Text2.
    Return: The shortest substring of Text1 that does not appear in Text2. (Multiple solutions may exist, in which case 
    you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    Text1 = input_lines[0]
    Text2 = input_lines[1]

    print(Shortest_NonShared_Substring(Text1, Text2))