import collections

money=0
X = int(input())  #fetch number of shoes
l = list(map(int,input().split()))   #list of available shoe sizes


N = int(input())   #number of customers
countobj = collections.Counter(l)


for i in range(N):
    ssize , price = map(int, input().split())
    if countobj[ssize] :              #if key is not present it returns 0 and 0 is considered as false in python
        l.remove(ssize)
        money += price
        countobj = collections.Counter(l)

        
print(money)
