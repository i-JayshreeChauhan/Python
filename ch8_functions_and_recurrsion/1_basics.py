
def avg():                   #this is function definition
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))
    d = int(input("Enter a number : "))

    avg = (a+b+c+d)/4
    print(f"avg value of {a},{b},{c} and {d} is = {avg}")

def avg(a,b,c,d=10):                   #this is function definition

    avg = (a+b+c+d)/4
    print(f"avg value of {a},{b},{c} and {d} is = {avg}")
    return avg


print(avg(1,2,3,4))    #this is function call
print(avg(1,2,3))    #this is function call