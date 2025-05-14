
with open("D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\t1.txt") as f:
    a=f.read()
    if a.lower().find("twinkle")!=-1:
        print("It contains 'twinkle' word.")
    else:
        print("It does not contains 'twinkle' word.")