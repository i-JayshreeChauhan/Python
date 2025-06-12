import collections

N = int(input())
supermarket = collections.OrderedDict()

for i in range(N):
    inp = input().split()

    if len(inp) == 3:
        item_name = inp[0] + " " + inp[1]
        price = int(inp[2])
    elif len(inp) == 2:
        item_name = inp[0] 
        price = int(inp[1])


    if item_name in supermarket:
        supermarket[item_name] += price
    else:
        supermarket[item_name] = price


#print(supermarket)

for key in supermarket:
    print(key,supermarket[key])