
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''

from datetime import date   # importing the date class from Python’s built-in datetime module. 
today =str( date.today() )   # in format YYYY-MM-DD


#----METHOD-1 

a = input("Enter Name : ")
a = letter.replace("<|Name|>",a)
a = a.replace("<|Date|>",today)

print(a)


#----- Method-2

b = input("Enter Name : ")
print(letter.replace("<|Name|>",b).replace("<|Date|>",today))

