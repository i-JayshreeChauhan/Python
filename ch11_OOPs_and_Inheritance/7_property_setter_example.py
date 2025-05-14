
class Student:

    @property                          #defines how it will be accessed
    def name(self):
        return self.name1
    
    @name.setter                       #defines how it will be modified / updated
    def name(self,val):
        self.name1 = val


s = Student()
s.name = "jayshree"
print(s.name)