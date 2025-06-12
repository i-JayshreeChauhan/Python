import itertools


K , M = input().split()
#print(K,M)
l = [] #emptylist
main_list = []

for i in range(int(K)):
    a,*l = input().split()
    l = list(map(int,l))
    main_list.append(l)
    #print(main_list)

max_val=0

func1 = lambda l : sum(i**2 for i in l) % int(M)

for i in itertools.product(*main_list):
    #print(list(i),end=" ")
    result = func1(list(i))
    if(result>max_val):
        max_val = result

#print("\n")
print(max_val)


