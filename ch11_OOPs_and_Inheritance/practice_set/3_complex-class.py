
class complex:
    img = 0 
    real = 0

    def __init__(self ,r, i):
        self.img = i
        self.real = r

    def show(self):
        print(f"{self.real} + {self.img}i ")

    def __add__(self,num):                 #operator overloading '+'

        c1 = complex(0,0)

        c1.img = self.img + num.img
        c1.real = self.real + num.real

        return c1
    
    def __mul__(self,num):                 #operator overloading '*'

        c1 = complex(0,0)

        c1.img = self.img * num.img
        c1.real = self.real * num.real

        return c1
    


c2= complex(2,2)
c3= complex(3,3)
c4 = c2 + c3
c4.show()

c4 = c2 * c3
c4.show()