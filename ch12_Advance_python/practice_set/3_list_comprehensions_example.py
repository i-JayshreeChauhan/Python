
# prepare a list having multiplication table value of user entered number

try :
    a = int(input("Enter a number : "))
except Exception as e:      #will catch error for any non number / any other type of error
    print(e)
else:  #executes when no error encountered
    
    
    table = [ (i*a) for i in range(1,11)]
    print(table)
    
    with open("D:\\0___LEARN\\Python\\ch12_Advance_python\\practice_set\\table.txt", "a") as f:
        f.write(f"table of {a} = {str(table)} \n" ) 

