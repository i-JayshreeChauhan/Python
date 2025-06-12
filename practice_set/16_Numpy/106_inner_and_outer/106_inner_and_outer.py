import numpy as np

A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(np.inner(A, B))
print(np.outer(A, B))
