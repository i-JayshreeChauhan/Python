
#write a program to rename a file "renamed_by_python.txt"

import os

# old file path
old_name = "D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\donkey_word_copy.txt"

# new file path
new_name = "D:\\0___LEARN\\Python\\ch9_File_io\\Practice_set\\renamed_by_python.txt"

# renaming the file
os.rename(old_name, new_name)

print("File renamed successfully.")