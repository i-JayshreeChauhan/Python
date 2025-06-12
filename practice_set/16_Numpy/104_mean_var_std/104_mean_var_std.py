import numpy as np

N,M = map(int,input().split())
l1 = []

for _ in range(N):
    l = list(map(int,input().split()))
    l1.append(l)

a1 = np.array(l1)

print(a1.mean(axis=1))
print(a1.var(axis=0))
print(round(a1.std(),11))
