
class Employee:
    id = 10                       #these are called class attributes
    salary = 1500000              #these are called class attributes

    def getdetails(self):                 #instead of self --you can use any other word  (however self is understandable)
        print(f"emp id = {self.id} and emp salary = {self.salary}.")

    def greet(self):           #self is a must pass argument       #instead of self --you can use any other word (however self is understandable)
        print("Hello!")

    def greet2(kkk):           #used kkk here inplace of self (works)
        print("Hello2!")

emp1 = Employee()
emp1.id=12    #instance/object attribute
emp1.salary = 1450000
emp1.getdetails()        # or Employee.getdetails(emp1) (both are same)
emp1.greet()
emp1.greet2()