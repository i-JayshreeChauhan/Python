import os
print(os.getcwd())   #shows current directory




try:
    f = open("D:\\0___LEARN\\Python\\ch9_File_io\\test1.txt")        #open function has by-defualt 'read' mode

    # f = open("D:\\0___LEARN\Python\ch9_File_io\\test1.txt" , "r")        #same as above expression

    data = f.read()
    print(data)
    f.close()
except:                             #executes at any exception calls  #or u can use --> except FileNotFoundError:   (this specifies type of error)
    print("File not found!")
