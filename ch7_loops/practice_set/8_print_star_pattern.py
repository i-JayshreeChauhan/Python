

'''
print below mentioned pattern

*****
*   *
*   *
*   *
*   *
*****
   ...ans so on
 
'''



n = int(input("Enter value from (3 to 10) : "))

if n>=3 :
    for i in range(1,n+1):
        if(i==1 or i==n):
            print("*" * n)
        elif(i>1 and i<n):
            print("*",end="")
            print(" " * (n-2),end="")
            print("*")
else:
    print("Pattern not possible!")
        


