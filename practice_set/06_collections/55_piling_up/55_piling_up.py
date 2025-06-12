from collections import deque
T = int(input())

for i in range(T):
    N = int(input())
    d = deque()
    l = list(map(int,input().split()))

    d.extend(l)
    #print(d)

    op = True
    loop = 0
    prev=0
    
    #compare last and first element
    while len(d) !=0 :
        a = d[0]
        b = d[len(d)-1]
        
        if loop==0:
            if a >= b :
                prev = d.popleft()
            else:
                prev = d.pop()
            loop+=1

        else:
            if a>prev or b>prev : 
                op = False
                break
            elif a<=prev or b<=prev:
                if a >= b :
                    prev = d.popleft()
                else:
                    prev = d.pop()
    
    if op:
        print("Yes")
    else:
        print("No")

