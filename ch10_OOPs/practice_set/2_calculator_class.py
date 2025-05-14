import math

class calculator:

    @staticmethod
    def sum(a,b):
        return a+b
    
    @staticmethod
    def subtraction(a,b):
        return a-b
    
    @staticmethod    
    def multiplication(a,b):
        return a*b

    @staticmethod
    def division(a,b):
        if(b==0):
            return -1
        else:
            return a/b

    @staticmethod
    def square(a):
        return a**2

    @staticmethod
    def cube(a):
        return a**3

    @staticmethod
    def squareroot(a):
        return math.sqrt(a)


calc = calculator()
print(calc.square(10))
print(calc.cube(10))
print(round(calc.squareroot(10),2))    #roundoff till 2 decimals
