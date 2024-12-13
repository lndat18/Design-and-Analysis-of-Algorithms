import os
import heapq

class Graph:
  def __init__(self):
    self.capacity = dict() # adjacency list
    self.V = 0
    self.E = 0
    self.source = 0
    self.sink = 0

  def __str__(self):
    res = 'V: %d, E: %d, source: %d, sink: %d\n'%(self.V, self.E, self.source, self.sink)
    for u, neighbors in self.capacity.items():
      line = '%d: %s\n'%(u, str(neighbors))
      res += line
    return res

  def print(self):
    print("---Thông tin đồ thị")
    print(str(self))

  def load_from_file(self, filename):
    if os.path.exists(filename):
      with open(filename) as g:
        self.V, self.E, self.source, self.sink = [int(it) for it in g.readline().split()]
        for i in range(self.E):
          line = g.readline()
          u, v, w = [int(it) for it in line.strip().split()]
          if u not in self.capacity:
            self.capacity[u] = []
          self.capacity[u].append((v, w))