import numpy as np

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

A = np.array(A)
B = np.array(B)

print(np.dot(A, B))
