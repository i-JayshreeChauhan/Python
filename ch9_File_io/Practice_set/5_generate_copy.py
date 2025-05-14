
#generate a copy of existing file

with open("D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\donkey_word.txt") as f:
    s = f.read()

path = "D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\donkey_word" + "_copy.txt"
with open(path , "w") as f:
    f.write(s)

