a=10
b=20.5


#--------------------------arithmatic operator

c = a+b        
print(c)

c=a*b       
print(c)

c=a/b        
print(c)

c=a-b       
print(c)


#--------------------------assignment operator
c= (a==b)
print(c)

c=0

c+= (a)
print(c)

#--------------------------comparision operator

c= (a>=b)
print(c)


c= (a!=b)
print(c)


#--------------------------logical operator

#for 'or' type of the input any input true , will result in true

c = True or True  #answer --> true
print(c)
c = True or False  #answer --> true
print(c)
c = False or True  #answer --> true
print(c)
c = False or False  #answer --> False
print(c)

c = (3==3) or (4==4)   # both true --result true
print(c)

c = (3==4) or (4==5)   # both false --result false
print(c)

# and --if both true - result true ,, if any input false result - false

c = True and True  #answer --> true
print(c)

c = True and False  #answer --> false
print(c)

c = False and False  #answer --> false
print(c)


#not operator returns opposite
c = not(False)
print(c)

c = not(True)
print(c)