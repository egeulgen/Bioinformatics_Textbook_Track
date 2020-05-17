import sys


def euclidean_distance(pointA, pointB):
    distance = 0
    for i in range(len(pointA)):
        distance += (pointA[i] - pointB[i]) ** 2
    distance = distance ** 0.5
    return distance


def distance_from_centers(centers, point):
    min_dist = float("Inf")
    for x in centers:
        current = euclidean_distance(x, point)
        if current < min_dist:
            min_dist = current
    return min_dist


def max_distance_point(data, centers):
    max_dist = -1
    for point in data:
        current = distance_from_centers(centers, point)
        if current > max_dist:
            max_dist = current
            max_point = point
    return max_point


def farthest_first_traversal(data, k):
    centers = [data[0]]
    while len(centers) < k:
        point = max_distance_point(data, centers)
        centers.append(point)
    return centers


if __name__ == "__main__":
    '''
    Given: Integers k and m followed by a set of points Data in m-dimensional space.
    Return: A set Centers consisting of k points (centers) resulting from applying FarthestFirstTraversal(Data, k), 
    where the first point from Data is chosen as the first center to initialize the algorithm.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, m = [int(x) for x in input_lines[0].split()]
    data = [[float(x) for x in line.split()] for line in input_lines[1:]]

    center_points = farthest_first_traversal(data, k)

    for center in center_points:
        print(" ".join(map(str, center)))
