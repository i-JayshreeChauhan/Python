n = int(input())
s1 = set() 
s1 = set(map(int,input().split()))

m = int(input())
s2 = set() 
s2 = set(map(int,input().split()))

print(len(s1.difference(s2)))
