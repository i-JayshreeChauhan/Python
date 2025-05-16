l1=[]  #empty list

for i in range(6):
    l1.append(int(input(f"Enter Marks of student {i+1} : ")))

l1.sort()
print(l1)


total = sum(l1)
print(total)
