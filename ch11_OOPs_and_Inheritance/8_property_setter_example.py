
class Student:

    @property
    def name(self):
        return f"first name : {self.fname}   last name : {self.lname}"           #instead of returning the string variable everytime (we are modifying it)
    
    @name.setter
    def name(self,val):
        self.fname = val.split(" ")[0]        #accessing the first element of list   #example : "jayshree chauhan"  -->after splitting using " " --> ['jayshree' , 'chauhan'] becomes list 
        self.lname = val.split(" ")[1]        #accessing the second element of list  # list : ['jayshree' , 'chauhan']


s = Student()
s.name = "chitrang vaniyawala"      #using a function as attribute (using @"attribute_name".setter function - to set values)
print(s.name)                       #using a function as attribute (@property -- for getting the value of attribute)


#----- Here there is process to segregate name into fname and lname ---which is not visible to user -hidden
#----- abstraction : showing what is essential to user and hiding stuff that should not be shown