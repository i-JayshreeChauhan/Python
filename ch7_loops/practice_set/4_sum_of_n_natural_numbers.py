
#do the sum of first n natural numbers using WHILE loop

a = int(input("Enter a number : "))
i = 1
sum = 0

while i<=a:
    sum += i 
    i+=1

print(f"sum till {a} numbers = {sum} ")