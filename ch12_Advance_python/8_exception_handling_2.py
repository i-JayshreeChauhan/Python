
try:
    l = [1,2,3]
    d = {'A' : 1 , "B" : 2 , "C" : 3}

    a = int(input("Enter number : "))  #valueError
    b = "2" + 3                        #typeError
    c = 1/0                            #ZeroDivisionError
    d = l[4]                           #IndexError
    
    e = d['j']                         #KeyError
    f = open("D:\\0___LEARN\\Python\\ch9_File_io\\te1.txt")  #FileNotFoundError

except ValueError as e1:   
    print(e1)
except TypeError as e2:   
    print(e2)
except ZeroDivisionError as e3:   
    print(e3)
except IndexError as e4:   
    print(e4)
except KeyError as e5:   
    print(e5)

except Exception as e6:  #general for all exception
    print(e6)