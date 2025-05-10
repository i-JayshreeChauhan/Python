a = "jayshree"
b = '''jayshree'''
c = """jayshree"""
d = 'jayshree'

print(a)
print(b)
print(c)
print(d)


#slicing a string

aa = "jayshree"
length = len(aa)
print("length of " , aa , " : " , length)

slicedstring = aa[1:5]  #this will slice the string starting from position 1 till 4 (5th is not included)    
print("sliced string : ",slicedstring)

slicedstring = aa[:5]  #this will slice the string starting from position 0 till 4th (5th is not included)      #same as aa[0:5]
print("sliced string : ",slicedstring)

slicedstring = aa[1:]  #this will slice the string starting from position 0 till last      #same as aa[1:8]
print("sliced string : ",slicedstring)

#negative slicing  (last char is -1 and second last -2 ......)
slicedstring = aa[-7:-3]
print("sliced string : ",slicedstring)

char1 = aa[3]
print("4th char : ",char1)

slicedstring = aa[1:7:2]                  # aa[1:7] --> ayshre    --> aa[1:7:2] --> "ayshre" --> skipping 2nd --> "asr"
print("sliced string : ",slicedstring)

bb="0123456789"
slicedstring = bb[1:9:3]   #bb[1:9]-->12345678 --> bb[1:9:3] --> "147" 
print("sliced string : ",slicedstring)