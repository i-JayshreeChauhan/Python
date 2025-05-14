# generate multiplication table from 2 to 6 in different files and keep this all files in a specific folder

for i in range(2,7):
    path = "D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\Multiplication_tables\\" + "table" + str(i) + ".txt"

    with open(path,"w") as f:
        #generate multiplication table
        s=f"Multiplication table of : {i}\n"
        for j in range(1,11):
            s+=f"{i} * {j} = {i*j}\n"
        f.write(s)    