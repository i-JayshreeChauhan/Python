T = int(input())

for i in range(0,T):
    eleA = int(input())
    A = set(map(int,input().split()))
    eleB = int(input())
    B = set(map(int,input().split()))

    A.difference_update(B)
    if len(A)==0:
        print("True")
    else:
        print("False")