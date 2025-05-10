

#----Note : list are mutable(modifyable) -- hence we can do all the mentioned things on fruits itself 
# (unlike strings that generates new strings after every method/operation/function on them)

fruits = []
print(type(fruits))   #this is an empty list

fruits = ["apple","banana","mango",-1.34,False,"grapes","watermelon"]
print(f"Original List : {fruits}")


#----Append

fruits.append("chickoo")
print(f"Modified List : {fruits}")


#----SORT

l1 = [1,3,5,7,6,2,9,3]
l1.sort()
print(l1)

#----REVERSE

l1 = [1,2,3,4,5,6]
l1.reverse()
print(l1)

#----length

print(len(l1))

#----Insert

l1 = [1,2,3,4,5,6]
l1.insert(3,111)   #adds 111 at index 3
print(l1)

#----Pop

l1 = [1,2,3,4,5,6]
l1.pop(3)   #pops 3rd index element
print(l1)

#----remove

l1 = [1,2,3,111,4,5,6]
l1.remove(111)   #removes 111
print(l1)


#----count

l1 = [1,2,3,1,111,4,1,5,6]

print(l1.count(1))
