
class Employee:
    salary = 10000
   

    @property
    def salary_after_increment(self):
        self.upd_salary = (( self.increment * self.salary ) + self.salary)
        return self.upd_salary 
    
    @salary_after_increment.setter
    def salary_after_increment(self,val):
        self.increment = (val * 0.01)


emp1 = Employee()
emp1.salary_after_increment = 20
print(emp1.salary_after_increment)