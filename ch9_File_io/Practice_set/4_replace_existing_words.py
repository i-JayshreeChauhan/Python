#write a program to read a file and replace word donkey / donkeys with ##### by updating the same file
s =""

with open("D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\donkey_word.txt") as f:
    s= f.read()
    result = s.lower().replace("donkey","######")

print(result)

with open("D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\donkey_word.txt","w") as f:
    f.write(result)