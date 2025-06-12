import collections 

n , m = map(int,input().split())
A = [] #empty list
B = [] #empty list

for i in range(n):
    A.append(input())

for i in range(m):
    B.append(input())

index_dict = collections.defaultdict(list)

for index,value in enumerate(A):
    index_dict[value].append(index+1)

#print(dict(index_dict))

for key in B:
    if key in index_dict:
        print(*index_dict[key])
    else:
        print("-1")
