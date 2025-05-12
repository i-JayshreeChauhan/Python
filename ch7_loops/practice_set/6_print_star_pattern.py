
'''
print below mentioned pattern

     *
    ***
   ***** 
   ...ans so on
 
'''



n = int(input("Enter value from (1 to 10) : "))
loop=1

for i in range(0,n):
    print(" " * (n-i-1) , end ="")
    print("*" * (i+loop), end ="")
    print(" " * (n-i-1))
    loop+=1

