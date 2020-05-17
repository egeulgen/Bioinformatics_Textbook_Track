class Tree:
    ''' Tree Structure
    '''
    def __init__(self):
        self.all_nodes = []
        self.all_edges = []
        self.root = self.add_node()

    class node:
        ''' Tree Node Structure
        '''
        def __init__(self):
            '''
            Each node has the following attributes:
            - label: node label
            - edges: list of edges from this node (edge objects)
            - indicator: (optional) if two stings are used for tree construction,
                an indicator is used to determine if the node corresponds to 
                a substring starting in Text1(#) or Text2($) or both (*)
            - depth: depth of node (by default 0)
            '''
            self.label = None
            self.edges = []
            self.indicator = None
            self.depth = 0

    class edge:
        ''' Tree Edge Structure
        '''
        def __init__(self):
            '''
            Each edge has the following attributes:
            - target_node: target node object
            - position: position of the substring in Text (used to construct the tree) belonging this edge
            - length: length of substring belonging to this edge
            '''
            self.from_node = None
            self.target_node = None
            self.position = None
            self.length = None
    
    def add_node(self):
        ''' Add a node
        Creates node newNode and adds this node to the tree
        Labels the new node with the next available integer
        (assuming root label is 0)
        '''
        newNode = Tree.node()
        newNode.label = len(self.all_nodes)

        self.all_nodes.append(newNode)

        return newNode

    def add_edge(self, from_node, target_node, pos, length):
        ''' Add an edge
        Creates edge newEdge from 'from_node' to 'target_node' with position 'pos'
        and length 'length'
        Updates depth attribute of 'target_node'
        Adds the new edge to 'from_node' and to the tree
        '''
        newEdge = Tree.edge()
        newEdge.from_node = from_node
        newEdge.target_node = target_node
        newEdge.position = pos
        newEdge.length = length

        target_node.depth = from_node.depth + length

        from_node.edges.append(newEdge)
        self.all_edges.append(newEdge)

        return newEdge

    def edge_labels(self, Text):
        ''' Method for returning all edge labels of
        the tree given Text
        '''
        edge_labels = []
        for edge in self.all_edges:
            edge_labels.append(Text[edge.position : edge.position + edge.length])
        return edge_labels

    def return_ripe_nodes(self):
        ''' Return all ripe nodes
        A node in a tree is called ripe if its indicator is None 
        but has no target nodes with None indicators.
        '''
        ripe_nodes = []
        for node in self.all_nodes:
            ripe_cond = False
            if node.indicator == None:
                ripe_cond = True
                for edge in node.edges:
                    if edge.target_node.indicator == None:
                        ripe_cond = False
                if ripe_cond:
                    ripe_nodes.append(node)
        return ripe_nodes

    def add_indicators(self):
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
        ripe_nodes = self.return_ripe_nodes()
        while len(ripe_nodes) != 0:
            for node in ripe_nodes:
                ## collect indicators for all children
                children_inds = []
                for edge in node.edges:
                    children_inds.append(edge.target_node.indicator)

                children_inds = list(set(children_inds))
                if len(children_inds) != 1:
                    node.indicator = '*' # if there exist children with differing indicators
                else: 
                    node.indicator = children_inds[0] # color of all children
            ripe_nodes = self.return_ripe_nodes()

    def construct_suffix_tree(self, trie_node, tree_node, path = []):
        ''' Recursive function for constructing suffix tree
        For each non-branching path Path in Trie:
             - substitute Path by a single edge e connecting the first and last nodes of Path
             - Position(e) ← Position (of first edge of Path)
             - Length(e) ← number of edges of Path
        '''
        # while trie node is non-branching, extend the path
        while len(trie_node.edges) == 1:
            trie_edge = trie_node.edges[0]
            path.append(trie_edge)
            trie_node = trie_edge.target_node

        # when the trie node is not 1-out,
        # terminate current path (if non-empty) and add to suffix tree
        if len(path) != 0:
            new_tree_node = self.add_node()
            _ = self.add_edge(tree_node, new_tree_node, path[0].position, len(path))
            tree_node = new_tree_node

        # if trie node is a leaf, add indicator to tree leaf and stop
        if len(trie_node.edges) == 0:
            tree_node.indicator = trie_node.indicator
            tree_node.label = trie_node.label
            return None

        # recursively apply over each target trie node
        for trie_edge in trie_node.edges:
            self.construct_suffix_tree(trie_edge.target_node, tree_node, [trie_edge])            
        

    def PopulateSuffixTree(self, Text):
        ''' Populate Suffix Tree
        Function construct suffix tree of Text 
        '''

        suffix_trie = Trie()
        suffix_trie.SuffixTrieConstruction(Text)
        self.construct_suffix_tree(suffix_trie.root, self.root)

    def __str__(self):
        ''' Custom __str__ method
        For printing the Tree as an adjacency list
        '''
        # header
        res = 'From->To:position:length\n\n'

        for edge in self.all_edges:
            res += str(edge.from_node.label) + '->' + str(edge.target_node.label) + ':' + str(edge.position) + ':' + str(edge.length) + '\n'

        return res

    def __repr__(self):
        return '<Tree object>'


class Trie:
    ''' Trie Structure
    '''
    def __init__(self):
        self.all_nodes = []
        self.all_edges = []
        self.root = self.add_node()

    class node:
        ''' Trie Node Structure
        '''
        def __init__(self):
            '''
            Each node has the following attributes:
            - label: node label
            - edges: list of edges from this node (edge objects)
            - indicator: (optional) if two stings are used for tree construction,
                an indicator is used to determine if the node corresponds to 
                a substring starting in Text1(#) or Text2($) or both (*)
            '''
            self.label = None
            self.edges = []
            self.indicator = None

    class edge:
        ''' Trie Edge Structure
        '''
        def __init__(self):
            '''
            Each edge has the following attributes:
            - target_node: target node object
            - label: label of this edge (symbol in Text)
            - position: position of the symbol in Text belonging this edge
            '''
            self.from_node = None
            self.target_node = None
            self.label = None
            self.position = None
    
    def add_node(self):
        ''' Add a node
        Creates node newNode and adds this node to the trie
        Labels the new node with the next available integer
        (assuming root label is 0)
        '''
        newNode = Trie.node()
        newNode.label = len(self.all_nodes)

        self.all_nodes.append(newNode)

        return newNode

    def add_edge(self, from_node, target_node, lbl, pos = None):
        ''' Add an edge
        Creates edge newEdge from 'from_node' to 'target_node' with position 'pos'
        and length 'length'
        Updates depth attribute of 'target_node'
        Adds the new edge to 'from_node' and to the tree
        '''
        newEdge = Trie.edge()
        newEdge.from_node = from_node
        newEdge.target_node = target_node
        newEdge.label = lbl
        newEdge.position = pos

        from_node.edges.append(newEdge)
        self.all_edges.append(newEdge)

        return newEdge

    def SuffixTrieConstruction(self, Text):
        ''' Suffix Trie Construction
        Construct the suffix trie of Text
        '''

        # from each possible position, iterate over all suffixes
        indicator = '#'
        for i in range(len(Text)):
            currentNode = self.root

            # iterate over each symbol in current suffix
            for j in range(i, len(Text)):
                currentSymbol = Text[j]

                # if there is an outgoing edge from currentNode labeled by currentSymbol
                # currentNode ← ending node of this edge
                found_in_edges = False
                for edge in currentNode.edges:
                    if edge.label == currentSymbol:
                        currentNode = edge.target_node
                        found_in_edges = True
                        break

                if not found_in_edges:
                    # add a new node newNode to Trie
                    newNode = self.add_node()
                    # add an edge from currentNode to newNode, labeled by currentSymbol and position j
                    _ = self.add_edge(currentNode, newNode, currentSymbol, j)

                    currentNode = newNode

            # if currentNode is a leaf in Trie, assign label i to this leaf
            if len(currentNode.edges) == 0:
                currentNode.label = 'L' + str(i)
                currentNode.indicator = indicator

            # change the indicator
            if Text[i] == '#':
                indicator = '$'
   
    def __str__(self):
        ''' Custom __str__ method
        For printing the Trie as an adjacency list
        '''
        # header
        res = 'From->To:label:position\n\n'

        for edge in self.all_edges:
            res += str(edge.from_node.label) + '->' + str(edge.target_node.label) + ':' + str(edge.label) + ':' + str(edge.position) + '\n'

        return res

    def __repr__(self):
        return '<Trie object>'