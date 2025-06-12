import numpy as np

N,M = map(int,input().split())
l1 = []
l2 = []

for _ in range(N):
    l = list(map(int,input().split()))
    l1.append(l)

A = np.array(l1)

for _ in range(N):
    l = list(map(int,input().split()))
    l2.append(l)

B = np.array(l2)


print(A+B) 
print(A-B) 
print(A*B) 
print(A//B) 
print(A%B) 
print(A**B) 