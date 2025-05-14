
def greatest_of_all(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    elif(c>=a and c>=b):
        return c   
    elif(a==b and a==c):
        return print("ALL VALUES ARE SAME")
    

print(greatest_of_all(1,4,7))