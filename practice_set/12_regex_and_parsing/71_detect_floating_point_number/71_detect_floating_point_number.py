import re

for _ in range(int(input())):
    s = input()

    pattern = r"^[+-]?(\d*\.\d+)$"
    print(bool(re.match(pattern,s)))