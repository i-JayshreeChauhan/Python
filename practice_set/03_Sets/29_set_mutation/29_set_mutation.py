n = int(input())
A = set(map(int,input().split()))  #main set

N = int(input())

set_list = [] #empty list

for i in range(0,N) :
    command,length = input().split()
    set_list.append(set(map(int,input().split())))

    if command.lower() == "intersection_update" :
        A.intersection_update(set_list[i])
    elif command.lower() == "difference_update" :
        A.difference_update(set_list[i])
    elif command.lower() == "symmetric_difference_update" :
        A.symmetric_difference_update(set_list[i])
    elif command.lower() == "update" :
        A.update(set_list[i])
    else:
        pass

print(sum(A))
