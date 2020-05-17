import sys


def HierarchicalClustering(distance_matrix, agg_method='average'):
    clusters = [[i] for i in range(len(distance_matrix))]

    new_clusters_list = []
    while len(clusters) != 1:

        ## Find the two closest clusters
        min_dist = float('inf')
        for i in range(len(clusters) - 1):
            for j in range(i + 1, len(clusters)):
                if agg_method == 'average':
                    dist = 0
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            dist += distance_matrix[idx1][idx2]
                    dist /= (len(clusters[i]) * len(clusters[j]))
                elif agg_method == 'min':
                    dist = float('inf')
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            current = distance_matrix[idx1][idx2]
                            if current < dist:
                                dist = current
                elif agg_method == 'max':
                    dist = -1
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            current = distance_matrix[idx1][idx2]
                            if current > dist:
                                dist = current
                else:
                    raise Exception('Agglomeration method not implemented!')
                if dist < min_dist:
                    min_dist = dist
                    closest_idx1 = i
                    closest_idx2 = j

        ## Merge the two closeet clusters
        new_cluster = clusters[closest_idx1] + clusters[closest_idx2]
        clusters = [clu for clu in clusters if clu not in [clusters[closest_idx1], clusters[closest_idx2]]]
        clusters.append(new_cluster)
        new_clusters_list.append(new_cluster)
    return new_clusters_list


if __name__ == "__main__":
    '''
    Given: An integer n, followed by an nxn distance matrix.
    Return: The result of applying HierarchicalClustering to this distance matrix (using Davg), with each newly created 
    cluster listed on each line.
    '''
    tmp = sys.stdin.read().splitlines()
    n = int(tmp[0])

    distance_matrix = []
    for i in range(1, len(tmp)):
        distance_matrix.append([float(d) for d in tmp[i].split(' ')])

    new_clusters_list = HierarchicalClustering(distance_matrix, 'average')
    for clu in new_clusters_list:
        print(' '.join([str(x + 1) for x in clu]))