
#find factorial of a number using reccursion

def factorial(n):
    if(n==1 or n==0): return 1
    f = factorial(n-1) * n
    return f

print(factorial(4))