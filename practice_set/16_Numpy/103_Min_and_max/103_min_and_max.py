import numpy as np

N,M = map(int,input().split())
l1 = []

for _ in range(N):
    l = list(map(int,input().split()))
    l1.append(l)

a1 = np.array(l1)
a2 = a1.min(axis=1)
#print(a2)
print(a2.max())
