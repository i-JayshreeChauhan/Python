

class Employee:
    company="ITC"
    Salary = 50000

    def show(self):
        print(f"Employee company = {self.company} and salary = {self.Salary}.")

class Manager(Employee):
    power = 10
    work = "managing"

class Programmer(Manager):
    name = "XYZ"

    def show2(self):
        print(f"Programmer company = {self.company} ,,, salary = {self.Salary} ,,,, name = {self.name},,,power ={self.power} ,,,, work = {self.work}")



p1 = Programmer()
p1.show2()

p1.power = 122
p1.work = "Programming + Managing"
p1.show2()