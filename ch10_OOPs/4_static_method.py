
class Employee:
    id = 10                       #these are called class attributes
    salary = 1500000              #these are called class attributes

    def getdetails(self):                 #instead of self --you can use any other word  (however self is understandable)
        print(f"emp id = {self.id} and emp salary = {self.salary}.")

    @staticmethod          #it is a decorator
    def greet():           #if you dont want to pass any argument , make it a static method   #it tells that this method doesnt require object as argument
        print("Hello!")



emp1 = Employee()
emp1.id=12    #instance/object attribute
emp1.salary = 1450000
emp1.getdetails()        # or Employee.getdetails(emp1) (both are same)
emp1.greet()
