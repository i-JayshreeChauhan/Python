
#instance/object attributes have higher preference than class attributes

class Employee:
    id = 10                       #these are called class attributes
    salary = 1500000              #these are called class attributes

emp1 = Employee()           #object declaration
emp1.name = "jayshree"      #these are object/instance attributes
emp1.salary = 1600000
print(emp1.name ," " , emp1.id , " " , emp1.salary)

emp2 = Employee()           #object declaration
emp2.name = "chitrang"       #these are object/instance attributes
emp2.id = 20
print(emp2.name ," " , emp2.id , " " , emp2.salary)