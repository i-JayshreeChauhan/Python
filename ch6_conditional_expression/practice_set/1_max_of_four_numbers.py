

a = int(input("Enter Number : "))
b = int(input("Enter Number : "))
c = int(input("Enter Number : "))
d = int(input("Enter Number : "))

if (a>=b and a>=c and a>=d):
    print(f"Max value : {a}")

elif (b>=a and b>=c and b>=d):
    print(f"Max value : {b}")

elif (c>=a and c>=b and c>=d):
    print(f"Max value : {c}")

else:
    print(f"Max value : {d}")
    