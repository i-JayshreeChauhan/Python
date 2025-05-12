
#-------------------- print multiplication table using for loop 

a = int(input("Enter Value : "))


for i in range(1,11):
    print(f" {a}*{i} = {a*i}")
else:
    print(f"--------Completed printing {a}'s table.")


#-------------------- print multiplication table using while loop 

b = int(input("Enter Value : "))
k=1

while k<11:
    print(f" {b}*{k} = {b*k}")
    k+=1

