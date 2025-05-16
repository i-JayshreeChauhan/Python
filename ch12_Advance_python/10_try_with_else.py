

try :
    f = open("D:\\0___LEARN\\Python\\ch9_File_io\\test1.txt")
    f.close()
except Exception as e:
    print(e)
else:
    print("In else block")        #else block runs if exception does not occur