import sys
import operator


class node:
    def __init__(self, lbl):
        self.label = lbl
        self.parent_nodes = []
        self.target_nodes = []
        self.visited = False


class DAG:
    def __init__(self):
        self.nodes_dict = {}
        self.distances = {}
        self.backtrack = {}

    def add_node(self, lbl):
        if lbl in self.nodes_dict:
            return self.nodes_dict[lbl]

        new_node = node(lbl)
        self.nodes_dict[lbl] = new_node
        return new_node

    def contruct_dag(self, adj_list_text):
        for line in adj_list_text:
            nodeA, tmp = line.split("->")
            nodeB, weight = tmp.split(":")
            weight = int(weight)

            from_node = self.add_node(nodeA)
            to_node = self.add_node(nodeB)

            from_node.target_nodes.append((to_node, weight))
            to_node.parent_nodes.append((from_node, weight))

    def topological_sort_util(self, node, stack):
        node.visited = True
        for node2,_ in node.target_nodes:
            if not node2.visited:
                self.topological_sort_util(node2, stack)
        stack.insert(0, node.label)

    def topological_sort(self):
        stack = []
        for node in self.nodes_dict.values():
            if not node.visited:
                self.topological_sort_util(node, stack)
        return stack

    def longest_path(self, source, sink):
        for label in self.nodes_dict:
            self.distances[label] = -float("Inf")

        self.distances[source] = 0
        self.backtrack[source] = None

        top_order = self.topological_sort()
        for label in top_order:
            current_node = self.nodes_dict[label]
            for v, weight in current_node.target_nodes:
                if self.distances[v.label] < self.distances[label] + weight:
                    self.distances[v.label] = self.distances[label] + weight
                    self.backtrack[v.label] = label

        path = [sink]
        curr = self.backtrack[sink]
        while curr != source:
            path = [curr] + path
            curr = self.backtrack[curr]
        path = [source] + path
        return self.distances[sink], path




if __name__ == "__main__":
    '''
    Given: An integer representing the source node of a graph, followed by an integer representing the sink node of the 
    graph, followed by an edge-weighted graph. The graph is represented by a modified adjacency list in which the 
    notation "0->1:7" indicates that an edge connects node 0 to node 1 with weight 7.
    Return: The length of a longest path in the graph, followed by a longest path. (If multiple longest paths exist, 
    you may return any one.)
    '''
    input_lines = sys.stdin.read().splitlines()
    source = input_lines[0]
    sink = input_lines[1]
    adj_list_text = input_lines[2:]

    graph = DAG()
    graph.contruct_dag(adj_list_text)
    longest_dist, longest_path = graph.longest_path(source, sink)
    print(longest_dist)
    print("->".join(longest_path))