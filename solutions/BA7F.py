import sys

ALPHABET = ['A', 'C', 'G', 'T']


def HammingDistance(p, q):
    mm = [p[i] != q[i] for i in range(len(p))]
    return sum(mm)


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def SmallParsimony(adj_list):
    ## initialize
    Tag = {}
    S = {}

    nodes = [item for sublist in adj_list for item in sublist]
    nodes = list(set(nodes))

    for v in nodes:
        S[v] = {}
        Tag[v] = 0
        if not RepresentsInt(v):
            Tag[v] = 1
            len_dna = len(v)
            for pos in range(len_dna):
                S[v][pos] = {}
                char = v[pos]
                for k in ALPHABET:
                    if char == k:
                        S[v][pos][k] = 0
                    else:
                        S[v][pos][k] = 1e6

    ## calculate scores
    while any(x == 0 for x in list(Tag.values())):
        zero_nodes = [node for node, tag in Tag.items() if tag == 0]
        for zn in zero_nodes:
            children = [child for parent, child in adj_list if parent == zn]
            if all([Tag[child] == 1 for child in children]):
                v = zn
                break
        Tag[v] = 1
        S[v] = {}
        for pos in range(len_dna):
            S[v][pos] = {}
            for k in ALPHABET:
                temp = []
                for i, score in S[children[0]][pos].items():
                    if i == k:
                        temp.append(score)
                    else:
                        temp.append(score + 1)
                score_daughter = min(temp)

                temp = []
                for i, score in S[children[1]][pos].items():
                    if i == k:
                        temp.append(score)
                    else:
                        temp.append(score + 1)
                score_son = min(temp)

                S[v][pos][k] = score_daughter + score_son
    return S


def FinalTree(adj_list, score_dict):
    nodes = [item for sublist in adj_list for item in sublist]
    nodes = list(set(nodes))
    child_nodes = [child for parent, child in adj_list]

    ## Find root
    root = nodes[0]
    idx = 1
    while root in child_nodes:
        root = nodes[idx]
        idx += 1

    ## Root's label and min parsimony score
    label_dict = {}
    label_dict[root] = ''
    min_pars_score = 0
    for pos, scores in score_dict[root].items():
        label_dict[root] += min(scores, key=scores.get)
        min_pars_score += min(scores.values())

    ## Backtrace
    Tag = {}
    for node in nodes:
        if not RepresentsInt(node):
            Tag[node] = 1
        else:
            Tag[node] = 0

    Tag[root] = 1

    while any(x == 0 for x in list(Tag.values())):

        one_nodes = [node for node, tag in Tag.items() if tag == 1]
        for node in one_nodes:
            children = [child for parent, child in adj_list if parent == node]
            if RepresentsInt(node) and all([Tag[child] == 0 for child in children]):
                v = node
                break

        daughter_label = ''
        daughter_scores = score_dict[children[0]]
        for pos, daughter_score in daughter_scores.items():
            parent_letter = label_dict[v][pos]
            # parent_score = score_dict[v][pos]
            # parent_score = parent_score[parent_letter]
            min_nucs = [nuc for nuc, val in daughter_score.items() if val == min(daughter_score.values())]
            if parent_letter in min_nucs:
                daughter_label += parent_letter
            else:
                daughter_label += min_nucs[0]

        label_dict[children[0]] = daughter_label
        Tag[children[0]] = 1

        son_label = ''
        son_scores = score_dict[children[1]]
        for pos, son_score in son_scores.items():
            parent_letter = label_dict[v][pos]
            # parent_score = score_dict[v][pos]
            # parent_score = parent_score[parent_letter]
            min_nucs = [nuc for nuc, val in son_score.items() if val == min(son_score.values())]
            if parent_letter in min_nucs:
                son_label += parent_letter
            else:
                son_label += min_nucs[0]

        label_dict[children[1]] = son_label
        Tag[children[1]] = 1

    ## Create final adjacency list
    final_adj_list = []
    for edge in adj_list:
        if RepresentsInt(edge[0]):
            node0 = label_dict[edge[0]]
        else:
            node0 = edge[0]
        if RepresentsInt(edge[1]):
            node1 = label_dict[edge[1]]
        else:
            node1 = edge[1]
        final_adj_list.append([node0, node1, HammingDistance(node0, node1)])
        final_adj_list.append([node1, node0, HammingDistance(node0, node1)])

    return [final_adj_list, min_pars_score]


if __name__ == "__main__":
    '''
    Given: An integer n followed by an adjacency list for a rooted binary tree with n leaves labeled by DNA strings.
    Return: The minimum parsimony score of this tree, followed by the adjacency list of the tree corresponding to 
    labeling internal nodes by DNA strings in order to minimize the parsimony score of the tree.
    '''
    lines = sys.stdin.read().splitlines()
    num_leaves = int(lines[0])

    adj_list = []
    for row in lines[1:]:
        temp = row.rstrip().split('->')
        adj_list.append(temp)

    score_dict = SmallParsimony(adj_list)

    final_adj_list, min_pars_score = FinalTree(adj_list, score_dict)

    print(min_pars_score)

    for edge in final_adj_list:
        print(str(edge[0]) + '->' + str(edge[1]) + ':' + str(edge[2]))