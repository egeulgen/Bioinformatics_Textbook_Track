import sys
from math import exp
from random import random


def Euclidean_distance(PointA, PointB):
    if len(PointA) != len(PointB):
        raise ValueError('The dimensions are not the same!')
    dist = 0
    for i in range(len(PointA)):
        dist += ((PointA[i] - PointB[i]) ** 2)
    dist **= 1/2
    return dist


def dist_from_centers(DataPoint, Centers):
    min_d = float("inf")
    for C in Centers:
        distance = Euclidean_distance(DataPoint, C)
        if distance < min_d:
            min_d = distance
    return min_d


def Random(prob_list):
    tot = sum(prob_list)
    massDist = map(lambda x: x/tot, prob_list)
    randRoll = random()
    cum = 0
    result = 0
    for mass in massDist:
        cum += mass
        if randRoll < cum:
            return result
        result += 1


def Hidden_Matrix(Data, Centers, beta):
    hidden_mat = [[0 for _ in range(len(Data))] for _ in range(len(Centers))]
    for j in range(len(Data)):
        tot = 0
        for i in range(len(Centers)):
            tot += exp(-beta * Euclidean_distance(Centers[i], Data[j]))
        for i in range(len(Centers)):
            hidden_mat[i][j] = exp(-beta * Euclidean_distance(Centers[i], Data[j])) / tot
    return hidden_mat


def clu_to_center(hidden_mat, Data):
    k = len(hidden_mat)
    m = len(Data[0])
    n = len(Data)
    new_centers = [[0 for j in range(m)] for i in range(k)]
    for i in range(k):
        for j in range(m):
            product = 0
            for idx in range(n):
                product += Data[idx][j] * hidden_mat[i][idx]
            new_centers[i][j] = product / sum(hidden_mat[i])
    return new_centers


def soft_kmeans(Data, k, beta, N=100):
    Centers = Data[:k]
    for _ in range(N):
        hidden_mat = Hidden_Matrix(Data, Centers, beta)
        Centers = clu_to_center(hidden_mat, Data)
    return Centers


if __name__ == "__main__":
    '''
    Given: Integers k and m, followed by a stiffness parameter β, followed by a set of points Data in m-dimensional 
    space.
    Return: A set Centers consisting of k points (centers) resulting from applying the soft k-means clustering 
    algorithm. Select the first k points from Data as the first centers for the algorithm and run the algorithm for 100 
    steps. Results should be accurate up to three decimal places.
    '''
    input_lines = sys.stdin.read().splitlines()
    k, m = [int(x) for x in input_lines[0].split(' ')]
    beta = float(input_lines[1])
    data = [[float(x) for x in line.split()] for line in input_lines[2:]]

    Centers = soft_kmeans(data, k, beta)
    for C in Centers:
        print(" ".join(map(str, C)))
