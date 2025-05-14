class Employee:
    
    id = 0                       #these are called class attributes
    salary = 0              #these are called class attributes


    def __init__(self,n,i,s):     #dunder method(starts from __) #this is a parameterized constructor #runs automatically when object is created  
        self.name = n
        self.id = i
        self.salary = s

"""
    def __init__(self):           #this is a parameterized constructor #runs automatically when object is created
        self.name = "e"
        self.id = 0
        self.salary = 100000
"""

        

emp1 = Employee("jayshree",10,1500000)           #object declaration
print(emp1.name ," " , emp1.id , " " , emp1.salary)

emp2 = Employee("chitrang",12,1750000)           #object declaration
print(emp2.name ," " , emp2.id , " " , emp2.salary)