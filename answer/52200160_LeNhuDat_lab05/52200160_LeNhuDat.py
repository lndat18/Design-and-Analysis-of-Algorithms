import argparse
import os


def Recursive_Insertion(arr: list, length: int) -> None:
    if length > 0:
        Recursive_Insertion(arr, length-1)
        index = length - 1
        val = arr[length]
        while index >= 0 and val < arr[index]:
            arr[index + 1] = arr[index]
            index -= 1
        arr[index + 1] = val


def Exp_squaring(a: int, n: int) -> int:
    if n == 1:
        return a
    if n % 2 == 0:
        return pow(Exp_squaring(a, n/2), 2)
    if n % 2 != 0:
        return pow(Exp_squaring(a, (n-1)//2), 2) * a
    

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


class Undirected_Graph:
    def __init__(self) -> None:
        self.AL = dict()
        self.V = 0
        self.E = 0
    

    def __str__(self) -> str:
        res = 'V: %d, E = %d\n' %(self.V, self.E)
        for u, neighbors in self.AL.items():
            line = '%d: %s\n' %(u, str(neighbors))
            res += line
        return res
    

    def print(self):
        print(str(self))


    def load_from_file(self, filename):
        with open(filename) as g:
            self.V, self.E = [int(it) for it in g.readline().split()]
            for line in g:
                u,v = [int(it) for it in line.strip().split()]
                if u not in self.AL:
                    self.AL[u] = []
                self.AL[u].append((v))

class Directed_Graph:
    def __init__(self) -> None:
        self.AL = dict()
        self.V = 0
        self.E = 0
    

    def __str__(self) -> str:
        res = 'V: %d, E = %d\n' %(self.V, self.E)
        for u, neighbors in self.AL.items():
            line = '%s: %s\n' %(u, str(neighbors))
            res += line
        return res
    

    def print(self):
        print(str(self))


    def load_from_file(self, filename):
        with open(filename) as g:
            self.V, self.E = [int(it) for it in g.readline().split()]
            for line in g:
                u,v = [it for it in line.strip().split()]
                if u not in self.AL:
                    self.AL[u] = []
                self.AL[u].append((v))
    
    def getVertexSet(self) -> set:
        res = {u for u in self.AL.keys()}
        for neighbors in self.AL.values():
            res.update(neighbors)
        return res


def DFS_search(g: Undirected_Graph, src: int, visited) -> None:
    visited[src] = 1
    
    print("%d " %(src), end='')

    for v in g.AL.get(src, []):
        if visited[v] == 0:
            DFS_search(g, v, visited)


def BFS_search(g: Undirected_Graph, src: int, visited) -> None:
    queue = [src]
    visited[src] = 1

    while len(queue) > 0:
        v = queue.pop(0)
        print("%d " %(v), end='')

        for u in g.AL.get(v, []):
            if visited[u] == 0:
                queue.append(u)
                visited[u] = 1


def TopoSearch(g: Directed_Graph, src: str, visited: dict, topo: list) -> None:
    visited[src] = 1
    for u in g.AL.get(src, []):
        if visited[u] == 0:
            TopoSearch(g, u, visited, topo)
    topo.append(src)


def DFS():
    g = Undirected_Graph()
    g.load_from_file('UDG.txt')
    visited = {v: 0 for v in g.AL.keys()}
    DFS_search(g, 0, visited)


def BFS():
    g = Undirected_Graph()
    g.load_from_file('UDG.txt')
    visited = {v: 0 for v in g.AL.keys()}
    BFS_search(g, 0, visited)


def TopoSort():
    g = Directed_Graph()
    g.load_from_file('DG.txt')
    vertex_set = g.getVertexSet()
    visited = {v: 0 for v in vertex_set}
    topo = []
    TopoSearch(g, 'A', visited, topo)
    topo.reverse()
    print(topo)


def LomutoPartition(arr: list, l: int, r: int) -> int:
    p = arr[r]
    s = l - 1
    for i in range(l, r):
        if arr[i] <= p:
            s += 1
            arr[i], arr[s] = arr[s], arr[i]
    arr[s + 1], arr[r] = arr[r], arr[s + 1]
    return s + 1


def QuickSelect(arr: list,l: int, r: int, k: int) -> int:
    if l <= r:
        s = LomutoPartition(arr, l, r)
        if s == k - 1:
            return arr[s]
        elif s > k - 1:
            return QuickSelect(arr, l, s - 1, k)
        else:
            return QuickSelect(arr, s + 1, r, k)


class Node:
    def __init__(self,data):
        self.left = self.right = None
        self.key = data


class BST:
    def __init__(self):
        self.root = None
      
    def __insert(self, root: Node, key):
        if root is None:
            return Node(key)
        cmp = key - root.key
        if cmp < 0:
            root.left = self.__insert(root.left, key)
        elif cmp > 0:
            root.right = self.__insert(root.right, key)
        return root
    
    def insert(self,key):
        self.root = self.__insert(self.root, key)

    def __search(self, root: Node, key) -> bool:
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.__search(root.left, key)
        else:
            return self.__search(root.right, key)

    def search(self, key) -> bool:
        return self.__search(self.root, key)

    def find_min(self) -> int:
        current = self.root
        if current is None:
            return None  # Cây rỗng
        while current.left:
            current = current.left
        return current.key

    def find_max(self) -> int:
        current = self.root
        if current is None:
            return None  # Cây rỗng
        while current.right:
            current = current.right
        return current.key


def BST_Algorithm():
    bst = BST()
    bst.insert(15)
    bst.insert(10)
    bst.insert(20)
    bst.insert(8)
    bst.insert(12)

    print(bst.search(10))  
    print(bst.search(5))  

    print(bst.find_min())  
    print(bst.find_max())  

    
def main():

    parser = argparse.ArgumentParser(description='Run functions.')
    parser.add_argument('--Recursive_Insertion', action='store_true') # Exercise 1
    parser.add_argument('--Exp_squaring', action='store_true') # Exercise 2
    parser.add_argument('--gcd', action='store_true') # Exercise 3
    parser.add_argument('--DFS', action='store_true') # Exercise 4
    parser.add_argument('--BFS', action='store_true') # Exercise 5
    parser.add_argument('--TopoSort', action='store_true') # Exercise 6
    parser.add_argument('--QuickSelect', action='store_true') # Exercise 7
    parser.add_argument('--BST_Algorithm', action='store_true') # Exercise 8

    args = parser.parse_args()

    if args.Recursive_Insertion:
        arr = [5,1,8,10,2,4,9] # len arr = 7
        Recursive_Insertion(arr, len(arr)-1)
        print(arr)
    elif args.Exp_squaring:
        a,n = 2,4
        res = Exp_squaring(a,n)
        print(res)
    elif args.gcd:
        print(gcd(10,20))
    elif args.DFS:
        DFS()
    elif args.BFS:
        BFS()
    elif args.TopoSort:
        TopoSort()
    elif args.QuickSelect:
        arr = [15,10,4,3,20,7]
        k = 6
        l = 0
        r = len(arr) - 1
        res = QuickSelect(arr, l, r, k)
        print(res)
    elif args.BST_Algorithm:
        BST_Algorithm()

if __name__ == '__main__':
    main()