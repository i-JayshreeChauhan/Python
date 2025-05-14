
class Employee:
    company="ITC"
    Salary = 50000

    def show(self):
        print(f"Employee company = {self.company} and salary = {self.Salary}.")
    

class Programmer(Employee):
    name = "XYZ"

    def show2(self):
        print(f"Programmer company = {self.company} ,,, salary = {self.Salary} ,,,, name = {self.name}.")



emp1 = Employee()
emp1.show()

prog1 = Programmer()
prog1.show()
prog1.show2()