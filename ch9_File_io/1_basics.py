
f = open("D:\\0___LEARN\\Python\\ch9_File_io\\test1.txt")
a = f.read()
print(a)
f.close()

print("--------------------")

f = open("D:\\0___LEARN\\Python\\ch9_File_io\\test1.txt")
b=f.readlines()          #returns list of lines present in file
print(b)
f.close()


print("--------------------")

f = open("D:\\0___LEARN\\Python\\ch9_File_io\\test1.txt")
b=f.readline()
print(b)

b=f.readline()
print(b)

f.close()
