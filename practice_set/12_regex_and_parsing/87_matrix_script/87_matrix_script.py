import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

#print(matrix)
tot = list(zip(*matrix))

#print(tot)

l = []  #empty list

for i in tot:
    l.append("".join(i))

Mainst = "".join(l)
#print(Mainst)

p1 = r'(?<=\w)[~`!@#$%^&*()\-_=+\[\]{}|\\;:\'",<.>/? ]+(?=\w)'

Mainst = re.sub(p1," ",Mainst)
print(Mainst)