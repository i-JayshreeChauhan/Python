
a = {} # empty dictionary
print(type(a))


#---we dont use {} to create empty set(as this will create empty dictionary) ---we use below mentioned method to create empty set

b = set()  #empty set
print(type(b))

s = {1,2,3,"jay",5,2,3,"123",44,22,7}     #set cannot have duplications
print(s)     #it will print set values without duplications --however order of elements may vary as it doesnt maintain that


#-----------Set Methods --------------------


#---add
s.add("XXXXXX")
print(s)

#---len
print(len(s))

#---pop
s.pop()
print(s)

#---remove
s.remove("jay")
print(s)