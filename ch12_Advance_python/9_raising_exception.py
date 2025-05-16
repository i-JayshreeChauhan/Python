try :
    a = int(input("Enter a number : "))
    b = int(input("Enter b number : "))

    if(b==0):
        raise ZeroDivisionError("Input b cannot be zero!")
    else:
        print(f"The division is {round((a/b),2)} ")

except ZeroDivisionError as e:
    print("Error : " , e)
except ValueError as e1:
    print("Error : " , e1)
