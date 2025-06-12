# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

data = ""
try:
    while True:
        line = input()
        data += line + "\n"
except EOFError:
    pass


p1 = r"\{(.*?)\}"
p2 = r"(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})"
matchlist1 = re.findall(p1, data, re.DOTALL)

for item in matchlist1:   
    s = item.strip()
    #print(s)
    matchlist2 = re.findall(p2,s)

    for i in matchlist2:
        print(i)