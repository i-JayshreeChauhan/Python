# list comprehensions is an elegent way to create list from existing list

l1 = [1,2,3,4,5]


#---------------------Method 1
#sq_l1=[]  #empty list
# for i in l1:
#     sq_l1.append(i**2)

#---------------------Method 2
sq_l1 = [i**2 for i in l1]

print(sq_l1)