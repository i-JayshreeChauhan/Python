aa = "JAYSHREE"
bb = "chitrang"
cc = " hello world "
dd = "hello i am jayshree.hello again from my side."
ee = "0133a4353312"
ff = "10390"

#####---------------- EVERY string function returns a NEW string ---doesnt modify the existing string as STRING in Python are immutable (cant update or change)

#identifying length of a string
v1 = len(aa)
print(v1)

#identifying last few items of a string
v2 = aa.endswith("AY")    #false
print(v2)

v2 = aa.endswith("HREE")    #true
print(v2)


#identifying first few items of a string
v2 = aa.startswith("AY")    #false
print(v2)

v2 = aa.startswith("JAY")    #True
print(v2)

#turning first char capital
print(bb.capitalize())

#Capitalizes the first letter of every word
print(dd.title())

#turning all char uppercase
print(bb.upper())

#turning all char lowercase
print(bb.lower())

#Removes leading and trailing whitespaces
print(cc.strip())


#Replaces all occurrences of a substring
print(dd.replace('hello','voila'))

#Splits a string into a list using a separator
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)

#Joins elements of an iterable into a single string
fruits = ['apple', 'banana', 'cherry']
text = "|".join(fruits)
print(text)

#Returns the index of the first occurrence of a substring (or -1)
print(dd.find("am"))


#Returns True if all characters are digits.
print(ee.isdigit())
print(ff.isdigit())

#Returns True if all characters are alphabets.
print(ee.isalpha())
print(aa.isalpha())


#count occurance of substring

print(ee.count('33'))
print(ee.count('33',0,8))    #start index , end index