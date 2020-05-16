import sys


class Node:
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

        new_node = Node(lbl)
        self.nodes_dict[lbl] = new_node
        return new_node

    def contruct_dag(self, adj_list_text):
        for line in adj_list_text:

            nodeA, tmp = line.split(" -> ")
            nodeB_list = tmp.split(",")

            from_node = self.add_node(nodeA)

            for nodeB in nodeB_list:
                to_node = self.add_node(nodeB)

                from_node.target_nodes.append(to_node)
                to_node.parent_nodes.append(from_node)

    def topological_sort_util(self, node, stack):
        node.visited = True
        for node2 in node.target_nodes:
            if not node2.visited:
                self.topological_sort_util(node2, stack)
        stack.insert(0, node.label)

    def topological_sort(self):
        stack = []
        for node in self.nodes_dict.values():
            if not node.visited:
                self.topological_sort_util(node, stack)
        return stack


if __name__ == "__main__":
    '''
    Given: The adjacency list of a graph (with nodes represented by integers).
    Return: A topological ordering of this graph.
    '''
    adj_list_text = sys.stdin.read().splitlines()

    graph = DAG()
    graph.contruct_dag(adj_list_text)
    print(", ".join(graph.topological_sort()))