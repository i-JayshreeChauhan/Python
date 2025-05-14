

class Employee:
    company="ITC"
    Salary = 50000

    def __init__(self):
        print("Employee constructor")

    def show(self):
        print(f"Employee company = {self.company} and salary = {self.Salary}.")

class Manager(Employee):
    power = 10
    work = "managing"

    def __init__(self):
        super().__init__()
        print("Manager constructor")

class Programmer(Manager):
    name = "XYZ"

    def __init__(self):
        super().__init__()
        print("Programmer constructor")

    def show2(self):
        print(f"Programmer company = {self.company} ,,, salary = {self.Salary} ,,,, name = {self.name},,,power ={self.power} ,,,, work = {self.work}")



p1 = Programmer()   #only programmer constructor runs
m1 = Manager()      #only Manager constructor runs
e1 = Employee()      #only Employee constructor runs

print("----------------------------")
# but if we use super (it makes parent/base class constructor to run)

p2 = Programmer()     #first manager constructor (base constructor) runs and then derived class constructor runs


print("----------------------------")

m2 = Manager()   #first Employee constructor (base constructor) runs and then derived class constructor runs