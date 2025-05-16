
#------------------- 1st

a= 23   #global variable
b=111

def func():
    global b    #calling global variable inside the func
    a=3   #local variable
    b=4
    print(a)
    print(b)

print(b)   #will print 111
func()   #will print 3 and 4
print(a)   #will print 23
print(b)   #will print 4         #this is because in func --we have called global b and then updated it to be 4




