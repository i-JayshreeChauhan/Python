

#----------- Example - 1
try:
    a = int(input("Enter a number : "))

except Exception as e:
    print(e)

print("-----test string ---- ")


#------------ Example - 2
try:
    f = open("D:\\0___LEARN\\Python\\ch9_File_io\\te1.txt")
except:
    print("file not found!")

print("-----test string  2---- ")