from functools import reduce

l = [1,4,7,2,3,6,2]

def max(a:int,b:int) -> int:
    if(a>=b):
        return a
    return b

max_val = reduce(max,l) 
print(max_val)