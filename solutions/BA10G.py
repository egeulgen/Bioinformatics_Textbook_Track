import sys
import HMMProfile_pseudocount

class Viterbi_Graph:
    ''' Viterbi Graph Structure
    Structure for storing Profile HMM
    '''

    def __init__(self):
        self.all_nodes = {}
        self.all_edges = []
        self.root = self.add_node()

    class node:
        ''' Node Structure
        '''
        def __init__(self):
            '''
            Each node has the following attributes:
            - label: label of node the (index, state) represented by the node
            - edges: list of edges from this node (edge objects)
            - parents: parent nodes of this node (node objects)
            - score: score to be calculated by Viterbi Algorithm
            - backtrace: the previous node that maximized the score
             (to be calculated by Viterbi Algorithm)
            '''
            self.label = None
            self.edges = []
            self.parents = []
            self.score = -1e6
            self.backtrace = None

    class edge:
        ''' Edge Structure
        '''
        def __init__(self):
            '''
            Each edge has the following attributes:
            - from_node: source node object
            - target_node: target node object
            '''
            self.from_node = None
            self.target_node = None
    
    def add_node(self, label = 'source'):
        ''' Add a node if it does not exist
        Creates node newNode and adds this node to the graph
        Labels the new node with the provided index and state (root is labeled as 'source')
        '''
        if self.node_exists(label):
            return self.all_nodes[label]
        
        newNode = Viterbi_Graph.node()
        newNode.label = label

        self.all_nodes[label] = newNode

        return newNode

        

    def add_edge(self, from_node, target_node):
        ''' Add an edge
        Creates edge newEdge from 'from_node' to 'target_node' 
        Adds the new edge to edges of 'from_node' and to the 
        all_edges attribute of the graph
        '''
        newEdge = Viterbi_Graph.edge()
        newEdge.from_node = from_node
        newEdge.target_node = target_node

        target_node.parents.append(from_node)
        from_node.edges.append(newEdge)
        self.all_edges.append(newEdge)

        return newEdge

    #### Helper methods
    def node_exists(self, label):
        if label in self.all_nodes.keys():
            return True
        return False

    #### Main methods
    def construct_graph(self, x, transition_matrix, emission_matrix):
        ''' Method to constuct the Viterbi graph
        from the HMM profile and the emitted string x
        '''

        ### Helper functions
        def parse_state(state):
            '''
            Function to parse each state (type and index)
            '''
            s_type = state.rstrip('0123456789')
            s_idx = state[len(s_type):]
            if s_type == 'S':
                s_idx = 0
            return s_type, int(s_idx) if s_idx != '' else -1


        # Determine states
        all_states = transition_matrix.keys()
        all_states = [state for state in all_states if state not in ['S', 'E']]

        max_state_idx = -1
        for state in all_states:
            s_type, s_idx = parse_state(state)
            if s_idx > max_state_idx:
                max_state_idx = s_idx

        ## num columns = emitted symbols + 1
        for idx in range(len(x) + 1):
            # initial column
            if idx == 0:
                current_node = self.root
                # add links to I0 and M1 from source
                ins_node = self.add_node((1, 'I0'))
                self.add_edge(current_node, ins_node)
                match_node = self.add_node((1, 'M1'))
                self.add_edge(current_node, match_node)
                
                # add deletion nodes and links to and from relevant nodes
                for state in all_states:
                    if state.startswith('D'):
                        # add link to previous node
                        next_node = self.add_node((idx, state))
                        self.add_edge(current_node, next_node)
                        current_node = next_node

                        # add link to insertion
                        del_type, del_idx = parse_state(state)
                        ins_node = self.add_node((1, 'I' + str(del_idx)))
                        self.add_edge(current_node, ins_node)
                        # add link to match
                        if del_idx != max_state_idx:
                            match_node = self.add_node((1, 'M' + str(del_idx + 1)))
                            self.add_edge(current_node, match_node)

            # rest
            else:
                for state in all_states:
    
                    self.add_node((idx, state)) # the method checks whether or not the node exists
                    current_node = self.all_nodes[(idx, state)]

                    # determine next possible states and add links
                    state_type, state_idx = parse_state(state)

                    # End state (i.e. sink node)
                    if idx == len(x):
                        if state_idx == max_state_idx:
                            next_node = self.add_node('sink')
                            self.add_edge(current_node, next_node)

                    # Others
                    else:

                        # deletion
                        del_state = 'D' + str(state_idx + 1)
                        if del_state in all_states:
                            next_node = self.add_node((idx, del_state))
                            self.add_edge(current_node, next_node)

                        # match
                        match_state = 'M' + str(state_idx + 1)
                        if match_state in all_states:
                            next_node = self.add_node((idx + 1, match_state))
                            self.add_edge(current_node, next_node)

                        # insertion
                        insertion_state = 'I' + str(state_idx)
                        if insertion_state in all_states:
                            next_node = self.add_node((idx + 1, insertion_state))
                            self.add_edge(current_node, next_node)

        return None

    def AlignmentWithProfileHMM(self, x, transition_matrix, emission_matrix):
        ''' Sequence Alignment with Profile HMM Problem
        Input: A string x followed by a threshold θ and a pseudocount σ, followed by an
        alphabet Σ, followed by a multiple alignment Alignment whose strings are formed from Σ. 
        Output: An optimal hidden path emitting x in HMM(Alignment, θ, σ).
        '''
        self.construct_graph(x, transition_matrix, emission_matrix)
        
        ## calculate all scores 
        self.root.score = 1
        string_idx = 0

        for column_idx in range(len(x) + 1):

            # find nodes in current column
            if column_idx == len(x) + 1:
                current_column = [self.all_nodes['sink']]
            else:
                current_column = []
                for node in self.all_nodes.values():
                    if node.label[0] == column_idx:
                        current_column.append(node)

            # calculate scores for each node in column
            for current_node in current_column:

                if current_node.label != "source":
                    current_state = current_node.label[1]
                    for parent_node in current_node.parents:

                        parent_state = 'S' if parent_node.label == 'source' else parent_node.label[1]

                        if current_state.startswith('D'):
                            tmp_score = parent_node.score * transition_matrix[parent_state][current_state]
                        else:
                            tmp_score = parent_node.score * transition_matrix[parent_state][current_state] * emission_matrix[current_state][x[string_idx]]
                        
                        if tmp_score > current_node.score:
                            current_node.score = tmp_score
                            current_node.backtrace = parent_node
            if column_idx != 0:
                string_idx += 1

        ## Backtrace the maximum scoring path
        final_nodes = self.all_nodes['sink'].parents

        max_score = -1e6
        for node in final_nodes:
            if node.score > max_score:
                max_score = node.score
                current_node = node

        optimal_hidden_path = []

        while current_node.label != 'source':
            optimal_hidden_path = [current_node.label[1]] + optimal_hidden_path
            current_node = current_node.backtrace
           
        return optimal_hidden_path

    def __str__(self):
        ''' Custom __str__ method
        For printing the Viterbi Graph as an adjacency list
        '''
        # header
        res = 'From->To:score(target)\n\n'

        for edge in self.all_edges:
            res += str(edge.from_node.label) + '->' + str(edge.target_node.label) + str(edge.target_node.score) + '\n'
        return res

    def __repr__(self):
        return '<Viterbi Graph adjacency list representation>'


if __name__ == "__main__":

    tmp = sys.stdin.read().splitlines()

    x = tmp[0]
    insertion_threshold, pseudocount = [float(x) for x in tmp[2].split()] # the insertion fraction threshold
    alphabet = tmp[4].split() # the alphabet that forms the strings in alignment
    
    # alignment 
    alignment = []
    for i in range(6, len(tmp)):
        alignment.append(tmp[i])

    transition_matrix, emission_matrix = HMMProfile_pseudocount.ProfileHMM(alignment, alphabet, insertion_threshold, pseudocount)

    ViterbiGraph = Viterbi_Graph()
    optimal_hidden_path = ViterbiGraph.AlignmentWithProfileHMM(x, transition_matrix, emission_matrix)

    print(' '.join(optimal_hidden_path))