import re
import email.utils

pattern = r"^([a-zA-Z][\w.-]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})$"


for _ in range(int(input())):
    data = input()
    name , mailid = email.utils.parseaddr(data)
    match = re.fullmatch(pattern,mailid)
    if match != None:
        print(data)

