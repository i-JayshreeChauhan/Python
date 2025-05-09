# write a python program to print the contents of the directory using the os module

import os

# Specify the directory path (current directory in this case)
directory_path = r"D:\0___LEARN"    #r--> raw --to consider \as path not special char

# Get the list of files and directories in the specified directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
