import sys


class Node:
    def __init__(self, label):
        self.label = label
        self.age = 0


class Tree:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, label):
        if label in self.nodes:
            return self.nodes[label]

        node = Node(label)
        self.nodes[label] = node
        return node

    def UPGMA(self, dist_mat, n):
        dist_dict = {}
        for i in range(len(dist_mat)):
            dist_dict[i] = {}
            for j in range(len(dist_mat[i])):
                dist_dict[i][j] = dist_mat[i][j]

        Clusters = {i: [i] for i in range(n)}

        for i in range(n):
            self.add_node(i)

        new_node_label = n
        T = []
        while len(dist_dict) > 1:
            min_dist = float("Inf")
            nodes = list(dist_dict.keys())
            for i in range(len(nodes) - 1):
                for j in range(i + 1, len(nodes)):
                    if dist_dict[nodes[i]][nodes[j]] < min_dist:
                        min_dist = dist_dict[nodes[i]][nodes[j]]
                        node_i = nodes[i]
                        node_j = nodes[j]

            new_cluster = Clusters[node_i] + Clusters[node_j]

            new_node = self.add_node(new_node_label)
            T.append([new_node_label, node_i])
            T.append([new_node_label, node_j])

            new_node.age = dist_dict[node_i][node_j] / 2

            dist_dict[new_node_label] = {}
            dist_dict[new_node_label][new_node_label] = 0
            for old_node in nodes:
                total = 0
                count = 0
                for init_node in Clusters[old_node]:
                    for node in new_cluster:
                        total += dist_mat[init_node][node]
                        count += 1
                dist_dict[old_node][new_node_label] = total / count
                dist_dict[new_node_label][old_node] = total / count

            Clusters[new_node_label] = new_cluster
            new_node_label += 1

            del dist_dict[node_i]
            del dist_dict[node_j]
            for key in dist_dict.keys():
                del dist_dict[key][node_i]

            for key in dist_dict.keys():
                del dist_dict[key][node_j]

        for edge in T:
            length = self.nodes[edge[0]].age - self.nodes[edge[1]].age
            self.edges.append(edge + [length])
            self.edges.append(edge[::-1] + [length])

        self.edges.sort(key=lambda x: x[1])
        self.edges.sort(key=lambda x: x[0])

        return self.edges


if __name__ == "__main__":
    '''
    Given: An integer n followed by a space-delimited n x n distance matrix.
    Return: An adjacency list for the ultrametric tree output by UPGMA. Weights should be accurate to three decimal 
    places.
    '''
    input_lines = sys.stdin.read().splitlines()
    n = int(input_lines[0])
    distance_matrix = [[int(x) for x in line.split()] for line in input_lines[1:]]

    t = Tree()
    adj_list = t.UPGMA(distance_matrix, n)

    for node1, node2, weight in adj_list:
        temp = str(node1) + '->' + str(node2) + ':' + str(round(weight, 3))
        print(temp)

