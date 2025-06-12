import itertools

s = input()

for key,i in itertools.groupby(s):
    l = [] #empty list
    length = len(list(i))
    l.append(length)
    l.append(int(key))

    print(tuple(l), end=" ")