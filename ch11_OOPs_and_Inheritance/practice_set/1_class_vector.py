# make a class of 2-d vectors and then make 3-d from it

class vector2d:
    dirx = 0
    diry = 0

    def __init__(self,x,y):
        self.dirx = x
        self.diry = y

    def showdirection(self):
        print(f"2D Direction of vector is {self.dirx}x + {self.diry}y")

class vector3d(vector2d):
    dirz = 0

    def __init__(self,x,y,z):
        self.dirx = x
        self.diry = y
        self.dirz = z 
    
    def showdirection(self):
        print(f"3D Direction of vector is {self.dirx}x + {self.diry}y + {self.dirz}z")

v1 = vector2d(51,10)
v1.showdirection()


v2 = vector3d(5,10,15)
v2.showdirection()