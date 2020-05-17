import sys
import queue


class Node:
    def __init__(self, label):
        self.label = label
        self.linked_nodes = set()


class Tree:
    def __init__(self):
        self.nodes_dict = {}

    def add_node(self, label):
        if label in self.nodes_dict:
            return self.nodes_dict[label]

        node = Node(label)
        self.nodes_dict[label] = node
        return node

    def construct_tree(self, adj_list):
        for line in adj_list:
            labels, weight = line.split(":")
            weight = int(weight)
            label1, label2 = [int(x) for x in labels.split("->")]

            node1 = self.add_node(label1)
            node2 = self.add_node(label2)

            node1.linked_nodes.add((label2, weight))
            node2.linked_nodes.add((label1, weight))

    def distance(self, label_a, label_b):
        visited = [False] * len(self.nodes_dict)
        distance = [0] * len(self.nodes_dict)

        Q = queue.Queue()
        distance[label_a] = 0

        Q.put(label_a)
        visited[label_a] = True
        while not Q.empty():
            x = Q.get()
            for label2, weight in self.nodes_dict[x].linked_nodes:
                if not visited[label2]:
                    distance[label2] = distance[x] + weight
                    Q.put(label2)
                    visited[label2] = True
        return distance[label_b]


    def distance_matrix_between_leaves(self, n_leaves):
        distance_mat = [[0 for _ in range(n_leaves)] for _ in range(n_leaves)]
        for i in range(n_leaves):
            for j in range(n_leaves):
                distance_mat[i][j] = self.distance(i, j)
        return distance_mat


if __name__ == "__main__":
    '''
    Given: An integer n followed by the adjacency list of a weighted tree with n leaves.
    Return: A space-separated n x n (di, j), where di, j is the length of the path between leaves i and j.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    adj_list = input_lines[1:]

    t = Tree()
    t.construct_tree(adj_list)
    result = t.distance_matrix_between_leaves(n)
    for row in result:
        print(" ".join(map(str, row)))