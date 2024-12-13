from itertools import combinations
from Graph import Graph
import numpy as np
import queue

class Problem(Graph):
    def __init__(self):
        self.coins = None
        super().__init__()

    def set_array(self, coins):
        self.coins = coins

    def set_graph(self, path):
        super().load_from_file(path)

    def get_array(self):
        return self.coins

    def get_graph(self):
        return super().__str__()

    def coin_row(self):
        if len(self.coins) == 0:    return 0

        F = [0] * (len(self.coins) + 1)
        F[0], F[1] = 0, self.coins[0]
        for i in range(2, len(self.coins) + 1):
            F[i] = max(self.coins[i - 1] + F[i - 2], F[i - 1])
        return F[-1]

    def extract_selected_coins(self, C):
        n = len(C)
        if n == 0:
            return []
        
        F = [0 for i in range(n + 1)]
        F[0] = 0
        F[1] = C[0]
        for i in range(2, n + 1):
            F[i] = max(C[i - 1] + F[i - 2], F[i - 1])
        selected = []
        i = n
        while i > 0:
            if F[i] == F[i - 1]:
                i -= 1
            else:
                selected.append(C[i - 1])
                i -= 2
        return selected[::-1]

    def shortest_augmenting_path(self):
        label = [0] * self.V
        q = queue.Queue()
        x = {i: {} for i in range(self.V)}
        for u in self.capacity:
            for v, cap in self.capacity[u]:
                x[u][v] = 0

        label[self.source - 1] = [float('inf'), '-']
        q.put(self.source)

        while not q.empty():
            i = q.get()
            for neighbor, cap in self.capacity.get(i, []):
                if label[neighbor - 1] == 0:
                    rij = cap - x[i][neighbor]
                    if rij > 0:
                        label[neighbor - 1] = [min(label[i - 1][0], rij), f'{i}+']
                        q.put(neighbor)

            for value in range(self.source, i):
                for neighbor, _ in self.capacity.get(value, []):
                    if neighbor == i:
                        if label[value - 1] == 0:
                            if x[value][i] > 0:
                                label[value - 1] = [min(label[i - 1][0], x[value][i]), f'{i}-']
                                q.put(value)

            if label[self.sink - 1] != 0:
                j = self.sink
                l_sink = label[j - 1][0]
                while j != self.source:
                    if '+' in label[j - 1][1]:
                        x[int(label[j - 1][1][0])][j] += l_sink
                    else:
                        x[j][int(label[j - 1][1][0])] -= l_sink
                    j = int(label[j - 1][1][0])

                label = [0] * self.V
                label[self.source - 1] = [float('inf'), '-']
                q = queue.Queue()
                q.put(self.source)
        return x

    def find_maximum_flow(self, x):
        return sum(x[i].get(self.sink, 0) for i in x)

    def find_minimum_cut(self, maximum, x):
        graph = dict()
        for u in self.capacity:
            graph[u] = {v: w for v, w in self.capacity[u]}
        
        cut_edges, maximum_cut = list(), 0
        for u in x:
            for v, w1 in x[u].items():
                if v in graph.get(u, {}):
                    w2 = graph[u][v]
                    if w1 == w2:
                        cut_edges.append((u, v, w1))
                        maximum_cut += w1

        if maximum_cut != maximum:
            list_cut_edges = list()

            for r in range(1, len(cut_edges) + 1):
                for comb in combinations(cut_edges, r):
                    total_weight = sum(item[2] for item in comb)
                    if total_weight == maximum:
                        list_cut_edges.append(comb)
            cut_edges = list()

            for cut_edge in list_cut_edges:
                new_graph = self.remove_cut_edges(self.capacity, cut_edge)
                
                if not self.bfs(new_graph, self.source, self.sink):
                    cut_edges.append(cut_edge)

        return cut_edges

    def remove_cut_edges(self, graph, cut_edges):
        new_graph = graph.copy()
        for edge in cut_edges:
            u, v, _ = edge
            new_graph[u] = [e for e in new_graph[u] if e[0] != v]
        return new_graph

    def bfs(self, graph, source, sink):
        visited = set()
        q = queue.Queue()
        q.put(source)
        while not q.empty():
            node = q.get()
            if node == sink:
                return True
            for neighbor, _ in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.put(neighbor)
        return False

    def adjacency_matrix(self):
        adj_matrix = np.zeros((self.V, self.V))
        out_flow, in_flow = [0] * self.V, [0] * self.V

        for i in self.capacity:
            for j, uij in self.capacity[i]:
                adj_matrix[i-1][j-1] = uij
                adj_matrix[j-1][i-1] = -uij

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix[0])):
                out_flow[i] += max(0, adj_matrix[i][j])
                in_flow[i] += max(0, adj_matrix[j][i])

        sink = out_flow.index(0) + 1
        source = in_flow.index(0) + 1

        return adj_matrix, source, sink