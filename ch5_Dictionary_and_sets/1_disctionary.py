

### dictionary is mutable

d={}  #---empty dictionary
print(type(d))

marks = {
    "jayshree" : 97,
    "chitrang" : 95,
    "kaushal" : 98,
    10 : [1,2,4]   #list
}

print(marks,type(marks))
print(marks["jayshree"])

print(marks[10])
#print(marks[13])    #this will throw error
print(marks.get(10))
print(marks.get(13))  #this wont throw error --if this key doesnt exist it will provide us None as reply

#---length

print(len(marks))

#---.items()
print(marks.items())    # it provides marks in the form of list of tuples

#---.keys()
print(marks.keys())    # it provides keys in the form of list 

#---.values()
print(marks.values())    # it provides values in the form of list 

#---.update()
marks.update({'chitrang':96 , 'kaushal':92 , 10:"hello" , 11:(1,2,3)})   #if we provide key which doesnt exist --it adds it
print(marks)

#----pop()
print(marks.pop('chitrang'))  # Removes 'chitrang' and returns its value
print(marks)

#----popitem()
print(marks.popitem())  # Removes last inserted item ---returns poped item
print(marks)

#----merging two dictionaries
d1 = { 1:"jay" , 2 : "chintu" , 3 : "kaushal" }
d2 = { 4:"richa" , 5 : "ankita" , 6 : "nishit" }

d1.update(d2)
print(d1)