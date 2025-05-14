
with (    #opening multiple files (update in newer python version)
    open("D:\\0___LEARN\Python\\ch9_File_io\\test1.txt") as f1,
    open("D:\\0___LEARN\Python\\ch9_File_io\\test2.txt") as f2
):
    print(f1.read())
    print("------------------")
    print(f2.read())