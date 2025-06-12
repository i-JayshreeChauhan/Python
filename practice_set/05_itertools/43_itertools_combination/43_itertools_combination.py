import itertools

st,k = input().split()
# print(st)
# print(k)

for r in range(1,int(k)+1):
    for i in itertools.combinations(sorted(st),r):
        print("".join(list(i)))