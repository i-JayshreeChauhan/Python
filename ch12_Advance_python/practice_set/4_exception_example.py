
try:
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of a : "))

    if(b==0):
        raise ZeroDivisionError("Input b cannot be zero!")
    else:
        print(f"The division is {round((a/b),2)} ")

except Exception as e:
    print(f"Error : {e} ")