
a = int(input("Enter number : "))
factorial = 1

for i in range(1,a+1):
    factorial *= i
else:
    print(f"Factorial of {a} = {factorial} ")