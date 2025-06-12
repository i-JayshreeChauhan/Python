import itertools

N = int(input())  
l = list(map(str,input().split()))
l.sort()
k = int(input())

#find permutations of 2 length
#itertools.permutations()
total_permutation = 0
matched_permutation = 0 
for i in itertools.combinations(l,k):
    if 'a' in list(i):
        matched_permutation+=1
    #print(list(i))
    total_permutation+=1

prob = float(matched_permutation) / float(total_permutation)
#print(matched_permutation)
#print(total_permutation)
print(prob)