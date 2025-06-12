# Output Format
# In the first line, print True if has any alphanumeric characters. Otherwise, print False .
# In the second line, print True if has any alphabetical characters. Otherwise, print False .
# In the third line, print True if has any digits. Otherwise, print False .
# In the fourth line, print True if has any lowercase characters. Otherwise, print False .
# In the fifth line, print True if has any uppercase characters. Otherwise, print False 


if __name__ == '__main__':
    s = input()

    #contains any alphanumeric char (a-z , A-Z , 0-9)
    if any(char.isalnum() for char in s):
        print("True")
    else:
        print("False")    


    #contains any alphabetical char (a-z , A-Z)
    if any(char.isalpha() for char in s):
        print("True")
    else:
        print("False")    


    #contains any digit (0-9)
    if any(char.isdigit() for char in s):
        print("True")
    else:
        print("False")    

    #contains any lowercase char (a-z)
    if any(char.islower() for char in s):
        print("True")
    else:
        print("False")    


    #contains any uppercase char (a-z)
    if any(char.isupper() for char in s):
        print("True")
    else:
        print("False")  