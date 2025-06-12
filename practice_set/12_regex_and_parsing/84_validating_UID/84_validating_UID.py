import re
pattern = r"^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$"


for _ in range(int(input())):
    s = set()  #empty set 
    uid = input()
    for i in uid:
        s.add(i)
    
    #print(len(s))
    
    if len(s)==10:
        match = re.fullmatch(pattern,uid)

        if match:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")


