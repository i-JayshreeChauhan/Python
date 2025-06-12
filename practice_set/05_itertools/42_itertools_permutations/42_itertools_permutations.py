import itertools

st,k = input().split()
# print(st)
# print(k)

for i in itertools.permutations(sorted(st),int(k)):
    print("".join(list(i)))