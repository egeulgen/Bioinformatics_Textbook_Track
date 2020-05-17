import sys
from BA8A import distance_from_centers


def squared_error_distortion(data, centers):
    distortion = 0
    for point in data:
        distortion += distance_from_centers(centers, point) ** 2
    distortion /= len(data)
    return distortion


if __name__ == "__main__":
    '''
    Given: Integers k and m, followed by a set of centers Centers and a set of points Data.
    Return: The squared error distortion Distortion(Data, Centers).
    '''
    input_lines = sys.stdin.read().splitlines()
    k, m = [int(x) for x in input_lines[0].split()]

    centers = [[float(x) for x in line.split()] for line in input_lines[1:k + 1]]
    data = [[float(x) for x in line.split()] for line in input_lines[k + 2:]]

    print(squared_error_distortion(data, centers))