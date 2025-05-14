
class Programmer:
    fav_lang="Python"
    id = 0
    salary = 10000

    def __init__(self,l="Java",i=10,s=1000000,n="XYZ"):     #constructor #dunder method
        self.fav_lang = l
        self.id = i
        self.salary = s
        self.name = n
    
    def printdata(self):
        print(f"Programmer Name : {self.name} --- Fav language : {self.fav_lang} --- id : {self.id} --- Salary : {self.salary}")
    


jayshree = Programmer("C++",3,1600000,"Jayshree")
jayshree.printdata()

chitrang = Programmer("Python",4,1750000,"Chitrang")
chitrang.printdata()


