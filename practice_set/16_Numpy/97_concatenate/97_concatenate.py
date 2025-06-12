import numpy as np
 
N,M,P = map(int,input().split())  #row1 # row2 #column

l1 = []  #empty list1
l2 = []  #empty list2

for _ in range(N):
    l = list(map(int,input().split()))
    l1.append(l)

a1 = np.array(l1)

for _ in range(M):
    l = list(map(int,input().split()))
    l2.append(l)

a2 = np.array(l2)

print( np.concatenate((a1,a2),axis=0))

