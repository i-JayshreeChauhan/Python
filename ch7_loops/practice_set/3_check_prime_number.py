
import math

#----- check whether given number is a prime number or not

a = int(input("Enter a number : "))

"""
Logic :

for finding any number x is prime or not
check whether it is divisible to any number till a number i*i < square(x)

example : check whether 37 is prime or not

6*6 < 37 ---> hence we will run the loop from 2 to 6 ---> if we find any number divisible to 37 (giving 0 remainder) ---it is not prime
else it is prime

"""

maxval = int(math.sqrt(a))      

# NOTE : else loop runs only when loop exits normally (not abruptly -one such is done using 'break')

for i in range (2,(maxval+1)):
        if(a%i==0):
            print(f"{a} is a prime number !!")
            break
else:
      print(f"{a} is NOT a prime number !!")