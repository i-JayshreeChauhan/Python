
try:
    with(
        open("D:\\0___LEARN\\Python\\ch12_Advance_python\\practice_set\\1.txt") as f1,
        open("D:\\0___LEARN\\Python\\ch12_Advance_python\\practice_set\\2.txt") as f2,
        open("D:\\0___LEARN\\Python\\ch12_Advance_python\\practice_set\\3.txt") as f3

    ):
        pass

except FileNotFoundError as e:
    print("File not found")
finally:
    print("This is a test msg")