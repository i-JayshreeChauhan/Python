
class calc:
    n=0

    def __init__(self,n):
        self.n = n
        
    def __add__(self,num):                  # operator overloading
        return self.n + num.n
    
    def __sub__(self,num):                  # operator overloading
        return self.n - num.n
    
    def __mul__(self,num):                  # operator overloading
        return self.n * num.n

    def __truediv__(self,num):              # operator overloading
        return self.n / num.n
    

c1 = calc(10)
c2 = calc(3)

print(c1+c2)
print(c1-c2)
print(c1*c2)
print(round((c1/c2) , 2))
