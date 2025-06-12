import numpy as np

l1 = []
l2 = []

for _ in range(int(input())):
    l = list(map(float,input().split()))
    l1.append(l)
    
a1 = np.array(l1)


print (round(np.linalg.det(a1),2))
