import numpy as np

l = input().split()       
x = float(input())        

a = np.array(list(map(float, l)))  # convert strings to float

print(np.polyval(a, x))   # Output: 3.0