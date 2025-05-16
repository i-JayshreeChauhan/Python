
### ----- map example

l = [1,2,3,4,5]

square = lambda x : x*x    #it will return square values

sqlist = map(square,l)      #implimenting a function on entire list
print(list(sqlist))


### ----- filter example

def even(n):
    if(n%2==0):
        return True
    return False

updlist = filter(even,l)
print(list(updlist))




### ----- reduce example

from functools import reduce

sum = lambda a,b : a+b   #used lambda function just for fun
print(reduce(sum,l))     # 1+2 --> 3 + 3 --> 6 + 4 --> 10 + 5 --> 15  (takes two items from list)


mult = lambda a,b : a*b   #used lambda function just for fun
print(reduce(mult,l))     #way of calculating factorial (1*2) --> 2*3 --> 6*4 --> 24*5 = 120