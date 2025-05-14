

##----Normal method

f = open("D:\\0___LEARN\\Python\\ch9_File_io\\test1.txt")
print(f.read())
f.close()

print("--------------------")


##----With method   --where you dont need to write f.close() explicitely

with open('D:\\0___LEARN\\Python\\ch9_File_io\\test1.txt') as f:
    print(f.read())


