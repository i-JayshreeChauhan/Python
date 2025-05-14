
a = "Hello jayshree ! How are you??"

f = open("D:\\0___LEARN\\Python\ch9_File_io\\test2.txt", "w")    # w = write
f.write(a)
f.close()


f = open("D:\\0___LEARN\\Python\\ch9_File_io\\test1.txt", "a")    # a = append
f.write(a)
f.close()