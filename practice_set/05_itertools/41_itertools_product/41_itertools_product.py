import itertools

l1 = list(map(int, input().split()))
l1.sort()

l2 = list(map(int, input().split()))
l2.sort()

#generating cartesiaan product

for i in itertools.product(l1,l2):
    print((i) , end=" ") 