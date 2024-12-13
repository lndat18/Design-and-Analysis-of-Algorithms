import argparse
import os
import heapq


class Graph:
    def __init__(self) -> None:
        self.AL = dict() # adjacency list
        self.EL = []
        self.V = 0
        self.E = 0
    

    def __str__(self):
        if self.AL:
            res = 'V: %d, E: %d\n'%(self.V, self.E)
            for u, neighbors in self.AL.items():
                line = '%d: %s\n'%(u, str(neighbors))
                res += line
        else:
            res = 'V: %d, E: %d\n'%(self.V, self.E)
            for u, v, w in self.EL:
                line = '%d %d %d\n'%(u,v,w)
                res += line
        return res
    

    def print(self):
        print(str(self))

    
    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                self.V, self.E = [int(it) for it in g.readline().split()]
                for _ in range(self.E):
                    line = g.readline()
                    u, v, w = [int(it) for it in line.strip().split()]
                    if u not in self.AL:
                        self.AL[u] = []
                    self.AL[u].append((v, w))


    def read_EL(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                self.V, self.E = [int(it) for it in g.readline().split()]
                count_real_edge = 0
                existing_edges = set() 
                for _ in range(self.E):
                    line = g.readline()
                    u, v, w = [int(it) for it in line.strip().split()]
                    if (u, v) not in existing_edges and (v, u) not in existing_edges:
                        count_real_edge += 1
                        existing_edges.add((u, v)) 
                        self.EL.append((u, v, w))  
                self.E = count_real_edge

class UnionFind:
    def __init__(self, size) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def ActivitySelection(activities: list) -> list:
    sorted_activities = sorted(activities, key=lambda x: x[1])
    activities_solution = []
    # get the first activity
    activities_solution.append(sorted_activities[0])
    j = 0
    for i in range(1, len(sorted_activities)):
        start, end = sorted_activities[i]
        _, end_solution = activities_solution[j]
        if end_solution < start:
            j += 1
            activities_solution.append((start,end))
    
    return activities_solution


def JobSequencing(task_deadline_profit: list) -> list:
    sorted_tdf = sorted(task_deadline_profit, key=lambda x: x[2], reverse=True)
    tdf_solution = [0] * len(sorted_tdf)
    i = 0 # i is one unit of time that each task take
    for task, dealine, profit in sorted_tdf:
        if tdf_solution[i] == 0:
            if dealine > i:
                tdf_solution.append((task, profit))
                i += 1
    tdf_solution = list(filter(lambda x: x != 0, tdf_solution))

    return tdf_solution 


def Prim(G: Graph, start_vertex = 0) -> list:
    visited = set()
    E_T = []
    PQ = []

    visited.add(start_vertex)
    for neighbor, weight in G.AL.get(start_vertex, []):
        heapq.heappush(PQ, (weight, start_vertex, neighbor))
    
    while PQ and len(visited) < G.V:
        weight, u, v = heapq.heappop(PQ)

        if v not in visited:
            visited.add(v)
            E_T.append((u, v, weight))

            for neighbor, w in G.AL.get(v, []):
                if neighbor not in visited:
                    heapq.heappush(PQ, (w, v, neighbor))

    return E_T


def kruskal(G: Graph) -> list:
    G.EL = sorted(G.EL, key=lambda edge: edge[2])
    
    uf = UnionFind(G.V)
    
    E_T = []
    
    for u, v, weight in G.EL:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            E_T.append((u, v, weight))
        
        if len(E_T) == G.V - 1:
            break

    return E_T


def main():
    parser = argparse.ArgumentParser(description='Run fucntions.')
    parser.add_argument('--ActivitySelection', action='store_true')
    parser.add_argument('--JobSequencing', action='store_true')
    parser.add_argument('--Prim', action='store_true')
    parser.add_argument('--kruskal', action='store_true')

    args = parser.parse_args()

    if args.ActivitySelection:
        activities = [(1,4),(3, 5), (0, 6), (5, 7), (3, 8), (5, 9), \
                      (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
        activities_solution = ActivitySelection(activities)
        print(activities_solution)
    
    elif args.JobSequencing:
        task_dl_profit = [(1,9,15), (2,2,2), (3,5,18), (4,7,1), (5,4,25),\
                          (6,2,20), (7,5,8), (8,7,10),(9,4,12), (10,3,5)]
        tdf_solution = JobSequencing(task_dl_profit)
        print(tdf_solution)

    elif args.Prim:
        g = Graph()
        g.load_from_file('Graph.txt')
        E_T = Prim(g)
        print(E_T)
    
    elif args.kruskal:
        g = Graph()
        g.read_EL('Graph.txt')
        E_T = kruskal(g)
        print(E_T)


if __name__ == '__main__':
    main()