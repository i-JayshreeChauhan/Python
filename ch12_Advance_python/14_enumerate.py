l1 = [111,333,555,777,999]

#-----------------Method 1
# index =0
# for i in l1:
#     print(f"The value at index {index} is {i}")
#     index +=1

#-----------------Method 2
for index,i in enumerate(l1):
    print(f"The value at index {index} is {i}")