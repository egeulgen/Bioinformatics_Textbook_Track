import sys
from Tree_Trie_classes import Trie

def TrieConstruction(Pattern_list):
    trie = Trie()

    for Pattern in Pattern_list:
        currentNode = trie.root

        for currentSymbol in Pattern:
            # if there is an outgoing edge from currentNode with label currentSymbol,
            # change currentNode to target_node
            for edge in currentNode.edges:
                if edge.label == currentSymbol:
                    currentNode = edge.target_node
                    break
            else:
                # add a new node newNode to Trie
                newNode = trie.add_node()
                # add a new edge from currentNode to newNode with label currentSymbol
                trie.add_edge(currentNode, newNode, currentSymbol)
                currentNode = newNode
    return trie


if __name__ == "__main__":
    '''
    Given: A collection of strings Patterns.
    Return: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has n nodes, 
    first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. 
    Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple 
    must be the integers labeling the initial and terminal nodes of the edge, respectively; the third member of the 
    triple must be the symbol labeling the edge.
    '''
    Patterns = sys.stdin.read().splitlines()
    trie = TrieConstruction(Patterns)

    for edge in trie.all_edges:
        print(str(edge.from_node.label) + '->' + str(edge.target_node.label) + ':' + str(edge.label))