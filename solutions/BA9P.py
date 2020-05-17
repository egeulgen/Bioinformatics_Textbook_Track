import sys
from re import split


class colored_Tree_node:
    ''' Colored Tree Node Structure
    Each node has children(list) and color (string) attributes.
    '''

    def __init__(self):
        self.children = []
        self.color = 'gray'


def is_node_ripe(tree_dict, node):
    ''' Check if node is ripe
    A node in a tree is called ripe if it is "gray" but has no "gray" children.
    '''
    if node.color != 'gray':
        return False

    for child_idx in node.children:
        if tree_dict[child_idx].color == 'gray':
            return False

    return True


def return_ripe_nodes(tree_dict):
    ''' Return ripe nodes in tree
    '''
    ripe_nodes = []
    for node_idx, node in tree_dict.items():
        if is_node_ripe(tree_dict, node):
            ripe_nodes.append(node)
    return ripe_nodes


def TreeColoring(tree_dict):
    ''' Tree Coloring
    # TreeColoring(ColoredTree)
    #     while ColoredTree has ripe nodes
    #         for each ripe node v in ColoredTree
    #             if there exist differently colored children of v
    #                 Color(v) ← "purple"
    #             else
    #                 Color(v) ← color of all children of v
    #     return ColoredTree
    '''

    ripe_list = return_ripe_nodes(tree_dict)
    while len(ripe_list) != 0:  ## while there are ripe nodes

        for ripe_node in ripe_list:
            ## collect colors for all children
            children_cols = []
            for child_idx in ripe_node.children:
                children_cols.append(tree_dict[child_idx].color)

            # if there exist differently colored children of v
            children_cols = list(set(children_cols))

            if len(children_cols) != 1:
                ripe_node.color = "purple"
            else:
                ripe_node.color = children_cols[0]  # color of all children

        ripe_list = return_ripe_nodes(tree_dict)

    return tree_dict


if __name__ == '__main__':
    '''
    Given: An adjacency list, followed by color labels for leaf nodes.
    Return: Color labels for all nodes, in any order.
    '''
    tmp = sys.stdin.read().splitlines()

    lst_flag = True

    tree_dict = {}
    for line in tmp:
        if line == '-':
            lst_flag = False

        elif lst_flag:
            tmp2 = split(' -> ', line)
            if tmp2[1] == "{}":
                tmp2[1] = []
            else:
                tmp2[1] = tmp2[1].split(',')

            node = colored_Tree_node()
            node.children = tmp2[1]
            tree_dict[tmp2[0]] = node

        else:
            tmp2 = split(': ', line)
            node = tree_dict[tmp2[0]]
            node.color = tmp2[1]

    tree_dict = TreeColoring(tree_dict)

    for node_idx, node in tree_dict.items():
        print(node_idx + ': ' + node.color)