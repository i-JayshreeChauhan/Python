
# Property and @.setter decorators are used for Encapsulation and abstraction 
#encapsulation (doing everything under one roof) (enclosing it) under class
#abstraction : do not show what is happening inside a function or thing (abstraction) -
# Abstraction in simple words is the concept of hiding the complex details of something and showing only the essential features to the user.

class Student:
    name = "something"
    id = 10

 #-------------------------- Normal way

    def set_age(self,val):
        self._age = val

    def get_age(self):
       return self._age


 #--------------------------with @property and @.setter decorators 
    @property
    def age(self):                   # It's accessed like an attribute
        return self._age 
    
    @age.setter      
    def age(self,val):
        self._age = val





#------------old method (using functions ---- user can easily understand this is a method defined in class)
s = Student()
s.set_age(12)
print(s.get_age())


#------------New method (using it like attribute ---- user can see that you are setting/using attribute , but actually fucntions are running in Background )
# way of abstraction

s1 = Student()
s1.age = 23
print(s1.age)