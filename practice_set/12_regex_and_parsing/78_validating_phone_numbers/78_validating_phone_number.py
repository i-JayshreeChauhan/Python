import re

pattern = r"^[789]\d{9}$"

for _ in range(int(input())) :
    match = re.fullmatch(pattern,input())
    if match != None:
        print("YES")
    else:
        print("NO")