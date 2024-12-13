import argparse
import numpy as np


def Binomial(n: int, k: int) -> int:
    C = np.zeros((n+1, k+1))
    for i in range(n+1):
        for j in range(min(i,k) + 1):
            if j == 0 or j == i:
                C[i, j] = 1
            else: C[i, j] = C[i-1, j-1] + C[i-1, j]
    print(C)
    return C[n, k]


def CoinRow(C: list) -> int:
    C.insert(0, 0)
    n = len(C)
    F = np.zeros(n)
    F[0] = 0
    F[1] = C[1]
    for i in range(2, n):
        F[i] = max(C[i] + F[i - 2], F[i-1])
    return F[n-1]


def changeMaking(D: list, n: int):
    F = np.zeros(n+1)
    D.insert(0,0)
    F[0] = 0
    for i in range(1, n+1):
        temp = float('inf')
        j = 1
        while j <= len(D)-1 and i >= D[j]:
            temp = min(F[i - D[j]], temp)
            j = j + 1
        F[i] = temp + 1
    return F[n]


def knapsack(w: int, v: int, max_W: int):
    n = len(w)
    F = np.zeros((n+1, max_W+1))
    for i in range(1, n+1):
        for j in range(max_W + 1):
            if j - w[i-1] >= 0:
                F[i,j] = max(F[i-1, j], v[i-1] + F[i-1, j - w[i-1]])
            else:
                F[i,j] = F[i-1, j]
    
    return F[n][max_W]



def main():
    # parser = argparse.ArgumentParser(description='Run Functions.')
    # parser.add_argument('--Binomial', action='store_true')
    # parser.add_argument('--CoinRow', action='store_true')
    # parser.add_argument('--changeMaking', action='store_true')
    # parser.add_argument('--knapsack', action='store_true')

    # args = parser.parse_args()

    # if args.Binomial:
    #     print(Binomial(10,2))
    # elif args.CoinRow:
    #     C = [5,1,2,1,6,2]
    #     CoinRow(C)
    # elif args.changeMaking:
    #     D = [1,3,5]
    #     n = 11
    #     print(changeMaking(D, n))
    # elif args.knapsack:
    #     w = [2,3,4,5]
    #     v = [3,4,5,6]
    #     max_W = 5
    #     print(knapsack(w,v,max_W))

    
    # EX1
    print(Binomial(10,2))
    # EX2
    C = [5,1,2,10,6,2]
    print(CoinRow(C))
    # EX3
    D = [1,3,5]
    n = 11
    print(changeMaking(D, n))
    # EX4
    w = [2,3,4,5]
    v = [3,4,5,6]
    max_W = 5
    print(knapsack(w,v,max_W))

        

if __name__ == '__main__':
    main()

