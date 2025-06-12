import itertools

st,k = input().split()
# print(st)
# print(k)

for i in itertools.combinations_with_replacement(sorted(st),int(k)):
        print("".join(list(i)))