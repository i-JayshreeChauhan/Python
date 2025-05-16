
###------ list are mutable(can change/update) ---tuple are immutable(cannot change/update)

fruits = ("banana","grapes","apple",123.4,-1,"watermelon")
print(type(fruits))

#-----what to do if tuple has only one element
jj=(1)
print(type(jj))   #it will show <class 'int'>

jj=(1,)
print(type(jj))   #it will show <class 'tuple'>

jj=()   #this is an empty tuple
print(type(jj))   #it will show <class 'tuplet'>   


#fruits[0] = 123  #---cant do ---will generate an error as tuples are immutable


#---Count
t1 = (1,11,2,22,3,33,4,44,4,4,25,44)
print(t1.count(4))

#---Index ---- this will return the index of 1st encounter of mentioned number/element
t1 = (1,11,2,22,3,33,4,44,4,4,25,44)
print(t1.index(4))

#---len
t1 = (1,11,2,22,3,33,4,44,4,4,25,44)
print(len(t1))

#---max
t1 = (1,11,2,22,3,33,4,44,4,4,25,44)
print(max(t1))


#---min
t1 = (1,11,2,22,3,33,4,44,4,4,25,44)
print(min(t1))

#---sort
t1 = (1,11,2,22,3,33,4,44,4,4,25,44)
print(sorted(t1))


#---concatination
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4)

#----Repetition --Repeats the tuple a given number of times.

t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)


#---slicing
t = (10, 20, 30, 40)
print(t[1:3])  # Output: (20, 30)


#---Unpacking ---Assigns tuple elements to variables.
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3

#---membership test --Checks if a value exists in the tuple.
t = (5, 10, 15)
print(10 in t)  # Output: True
