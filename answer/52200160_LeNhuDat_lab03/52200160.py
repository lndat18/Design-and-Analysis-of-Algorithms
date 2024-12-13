import numpy as np
import math 
from itertools import permutations
from itertools import combinations

def exponential_power(a, n):
    res = 1
    for i in range(1,n+1):
        res *= a
    return res


def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def C(k,n):
    return factorial(n)/((factorial(k))*factorial(n-k))


def matrixMul(arr1, arr2):
    row = len(arr1[0])
    col = len(arr2)
    result = np.zeros((row, col))
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result


def distance(x,y):
    d = 0.0
    sum_square = (x[0] - y[0])**2 + (x[1] - y[1])**2
    return math.sqrt(sum_square)


def closet_pair(list_point):
    dmin = float('inf')
    im = -1
    jm = -1
    for i in range(len(list_point)-1):
        for j in range(i+1, len(list_point)):
            d = distance(list_point[i], list_point[j])
            if d < dmin:
                dmin = d
                im = i
                jm = j
    return im,jm


def equation_line(pointA, pointB):
    x1,y1 = pointA
    x2,y2 = pointB
    a = y1 - y2
    b = x2 - x1
    c = x1*y2 - x2*y1
    return a,b,c


def distance_cvHull(point, a, b, c):
    x,y = point
    return (a*x + b*y + c)/(math.sqrt((a**2) + (b**2)))


def is_all_on_one_side(points, a,b,c,i,j):
    dist = [distance_cvHull(points[k],a,b,c) for k in range(len(points)) if k != i and k != j]
    if all(d > 0 for d in dist) or all(d < 0 for d in dist):
        return True
    return False


def convex_hull(points):
    hull = set()
    for i in range(len(points)-2):
        for j in range(i+1, len(points)):
            a,b,c = equation_line(points[i], points[j])
            if is_all_on_one_side(points,a,b,c,i,j):
                hull.update((points[i], points[j]))
    return hull            
    

def calculate_path_weight(path, graph):
    weight = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        for neighbor, w in graph[u]:
            if neighbor == v:
                weight += w
                break
    start, end = path[0], path[-1]
    for neighbor, w in graph[end]:
        if neighbor == start:
            weight += w
            break
    return weight


def tsp_brute_force(graph):
    vertices = list(graph.keys()) 
    min_path = None
    min_weight = float('inf')
    
    for perm in permutations(vertices):
        current_weight = calculate_path_weight(perm, graph)
        
        if current_weight < min_weight:
            min_weight = current_weight
            min_path = perm
            
    return min_path, min_weight


def knapsack_brute_force(weights, values, K):
    n = len(weights)
    max_value = 0
    best_subset = []
    
    for r in range(n + 1):
        for subset in combinations(range(n), r):
            total_weight = sum(weights[i] for i in subset)
            total_value = sum(values[i] for i in subset)
            
            if total_weight <= K:
                if total_value > max_value:
                    max_value = total_value
                    best_subset = subset
                    
    return best_subset, max_value


def main():
    A = [[1,1,1],
         [2,2,2],
         [3,3,3]]
    
    B = [[1,1,1],
         [1,1,1],
         [1,1,1]]
    
    # warm up exercise
    # print(exponential_power(2,4))
    # print(C(2,6))
    # print(matrixMul(A, B))


    # closest paire
    # list_point = [(1,30), (13,0), (40,5), (5,1), (12,10), (3,4)]
    # x,y = closet_pair(list_point)
    # print(list_point[x], list_point[y])

    # convex hull
    # points = [(0,3), (2,3), (1,1), (2,1), (3,0), (0,0), (3,3)]
    # print(convex_hull(points))

    # TSP
    # G = {1: [(2,4), (3,3), (4,1)],
    #      2: [(1,4), (3,1), (4,2)],
    #      3: [(1,3), (2,1), (4,5)],
    #      4: [(1,1), (2,2), (3,5)]}
    # path, weight = tsp_brute_force(G)
    # print(path, weight)


    # knapsack
    weights = [2, 3, 4, 5]  
    values = [3, 4, 5, 6]   
    K = 5  
    best_items, max_value = knapsack_brute_force(weights, values, K)
    print(best_items, max_value)


if __name__ == '__main__':
    main()