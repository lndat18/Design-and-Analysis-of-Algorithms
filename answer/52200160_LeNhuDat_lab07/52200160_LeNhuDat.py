import numpy as np
import argparse
import os


class Graph:
    def __init__(self) -> None:
        self.V = 0
        self.AM = None
    
    
    def read_graph(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                self.V = int(g.readline().strip())
                self.AM = np.zeros((self.V, self.V))
                for i in range(self.V):
                    line = g.readline().strip().split()
                    for j in range(self.V):
                        self.AM[i, j] = int(line[j])

    
    def read_graph2(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                self.V = int(g.readline().strip())
                self.AM = np.zeros((self.V, self.V))
                for i in range(self.V):
                    line = g.readline().strip().split()
                    for j in range(self.V):
                        if line[j] == 'inf':
                            self.AM[i, j] = float(line[j])
                        else:
                            self.AM[i, j] = int(line[j])
                    
    
    def __str__(self):
        res = f'Vertices: {self.V}\nAdjacency Matrix:\n{self.AM}'
        return res
        

    def print(self):
        print(str(self))


def LCS_Length(A: list,B: list):
    n, m = len(A), len(B)
    length = np.zeros((n, m))
    topleft, top, left = 1,2,3
    prev = np.zeros((n, m))
    
    for i in range(1,n):
        for j in range(1,m):
            if A[i] == B[j]:
                length[i ,j] = length[i-1,j-1] + 1
                prev[i,j] = topleft
            elif length[i-1, j] >= length[i, j-1]:
                length[i,j] = length[i-1,j]
                prev[i,j] = top
            else:
                length[i, j] = length[i,j-1]
                prev[i,j] = left

    return length[n-1, m-1], prev


def Output_LCS(A, prev, i, j):
    if i == 0 or j == 0:
        return
    if prev[i, j] == 1:
        Output_LCS(A, prev, i-1, j-1)
        print(A[i])
    elif prev[i, j] == 2:
        Output_LCS(A, prev, i-1, j)
    else:
        Output_LCS(A, prev, i, j-1)


def Warshall(filename):
    g = Graph()
    g.read_graph(filename)
    A = g.AM.copy()
    for k in range(g.V):
        for i in range(g.V):
            for j in range(g.V):
                A[i, j] = A[i, j] or (A[i, k] and A[k, j])
    return A


def Floyd(filename):
    g = Graph()
    g.read_graph2(filename)
    D = g.AM.copy()
    P = np.zeros((g.V, g.V))
    for k in range(g.V):
        for i in range(g.V):
            for j in range(g.V):
                D[i, j] = min(D[i, j], D[i, k] + D[k, j])
    return D


def Floyd_path(filename):
    g = Graph()
    g.read_graph2(filename)
    D = g.AM.copy()
    P = np.zeros((g.V, g.V), dtype=int)

    # initializing the P
    for i in range(g.V):
        for j in range(g.V):
            if D[i, j] == float('inf'):
                P[i, j] = -1
            else:
                P[i, j] = j

    # # Floyd
    for k in range(g.V):
        for i in range(g.V):
            for j in range(g.V):
                if (D[i, k] == float('inf') or D[k, j] == float('inf')):
                    continue
                if (D[i, j] > D[i, k] + D[k, j]):
                    D[i, j] = D[i, k] + D[k, j]
                    P[i, j] = P[i, k]
    return P


def getPath(P, start, end):
    if P[start, end] == -1:
        return None
    
    path = [start]
    while start != end:
        start = int(P[start, end])
        path.append(start)

    return path


def main():
    parser = argparse.ArgumentParser(description='Run functions.')
    parser.add_argument('--Output_LCS', action='store_true')
    parser.add_argument('--Warshall', action='store_true')
    parser.add_argument('--Floyd', action='store_true')
    parser.add_argument('--Floyd_path', action='store_true')


    args = parser.parse_args()

    if args.Output_LCS:
        A, B = "BAHXKZ", "ABXHZ"
        A, B = list(A), list(B)
        A.insert(0,0)
        B.insert(0,0)
        x, y = LCS_Length(list(A), list(B))
        print(x)
        i,j = len(A), len(B)
        Output_LCS(A, y, i-1, j-1)

    elif args.Warshall:
        A = Warshall('Graph.txt')
        print(A)

    elif args.Floyd:
        D = Floyd('Graph2.txt')
        print(D)

    elif args.Floyd_path:
        P = Floyd_path('Graph2.txt')
        print(P)
        path = getPath(P, 0, 4)
        print(path)

if __name__ == '__main__':
    main()