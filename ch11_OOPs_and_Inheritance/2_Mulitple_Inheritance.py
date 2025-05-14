class Employee:
    company="ITC"
    Salary = 50000

    def show(self):
        print(f"Employee company = {self.company} and salary = {self.Salary}.")
    
class Manager:
    power = 10


    

class Programmer(Employee,Manager):
    name = "XYZ"

    def show2(self):
        print(f"Programmer company = {self.company} ,,, salary = {self.Salary} ,,,, name = {self.name},,, Power = {self.power}")



p1 = Programmer()
p1.show2()
p1.company = "ABC"
p1.Salary = 55555
p1.power = 50

p1.show2()
