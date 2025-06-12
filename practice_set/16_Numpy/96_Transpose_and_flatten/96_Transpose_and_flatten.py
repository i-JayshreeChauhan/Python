import numpy as np 

N,M = map(int,input().split())
main_list = []

for _ in range(N):
    l = list(map(int,input().split()))
    main_list.append(l)
    
a1 = np.array(main_list)
print(a1.T)
print(a1.flatten())



