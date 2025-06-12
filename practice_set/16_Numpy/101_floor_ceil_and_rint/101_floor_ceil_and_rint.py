import numpy as np
np.set_printoptions(legacy='1.13')

l = list(map(float,input().split()))
a1 = np.array(l)


print(np.floor(a1))
print(np.ceil(a1))
print(np.rint(a1))

