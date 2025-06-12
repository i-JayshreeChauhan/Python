from collections import OrderedDict

N = int(input())
words = OrderedDict()  #defining empty ordered dictionary
init_count=1


for _ in range(N):
    w = input()

    if w not in words:
        words[w]= init_count
    else:
        words[w] += 1  

print(len(words))  #number of distinct words

for key in words:
    print(words[key] , end=" ")