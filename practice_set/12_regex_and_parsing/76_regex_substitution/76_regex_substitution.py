
import re

p1 = r"(?<= )&&(?= )"
p2 = r"(?<= )\|\|(?= )"

for i in range(int(input())):
    line = input()
    line = re.sub(p1,"and",line)
    line = re.sub(p2,"or",line)
    print(line)



