import sys
from collections import defaultdict
from BA8A import euclidean_distance


def closest_center(point, centers):
    min_dist = float("Inf")
    for x in centers:
        current = euclidean_distance(x, point)
        if current < min_dist:
            min_dist = current
            closest = x
    return closest


def cluster_mean(cluster):
    m = len(cluster[0])
    center = [0] * m
    for point in cluster:
        for i in range(m):
            center[i] += point[i]
    center = [x / len(cluster) for x in center]
    return center


def lloyd_k_means(data, k):
    centers = data[:k]

    while True:
        # Centers to clusters
        cluster_assignments = defaultdict(list)
        for point in data:
            center = closest_center(point, centers)
            cluster_assignments[tuple(center)].append(point)

        # Clusters to centers
        new_centers = [[]] * k
        for i in range(k):
            new_centers[i] = cluster_mean(cluster_assignments[tuple(centers[i])])

        if new_centers == centers:
            break
        centers = new_centers[:]

    return centers


if __name__ == "__main__":
    '''
    Given: Integers k and m followed by a set of points Data in m-dimensional space.
    Return: A set Centers consisting of k points (centers) resulting from applying the Lloyd algorithm to Data and 
    Centers, where the first k points from Data are selected as the first k centers.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, m = [int(x) for x in input_lines[0].split()]
    data = [[float(x) for x in line.split()] for line in input_lines[1:]]

    centers = lloyd_k_means(data, k)
    for center in centers:
        print(" ".join(map(str, center)))
