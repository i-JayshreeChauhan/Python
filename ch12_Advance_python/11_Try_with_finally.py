
# here finally block will run regardless of exception occurs or not
try :
    f = int(input("Enter number : "))
except Exception as e:
    print(e)
else:
    print("In else block")
finally:                                    #runs irrespective of any logic
    print("inside 'finally' block")



print(" ")
print(" ")

##-----MAIn use of finally occurs when running inside any function

def divide(a,b):
    try :
        c = a/b
        print(c)
        return c
    except Exception as e:
        print("--> Exception occured")
        return -1
    finally:
        print("this always runs (even after return is instructed from function)")


divide(6,3)
print(" ")
print(" ")
divide(3,0)
print(" ")
print(" ")
divide(2,4)
print(" ")
print(" ")
divide(3,0)
    