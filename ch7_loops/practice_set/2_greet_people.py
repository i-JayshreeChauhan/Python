
#greet people mentioned in list (whose name starts with S)

l1 = [ "jayshree" , "shyam" , "kaushal" , "sarita" , "vidhya" , "chitrang" , "sachin"]

for i in l1:
    
    if i.lower().startswith('s'):
        print(f"Hello {i} !")