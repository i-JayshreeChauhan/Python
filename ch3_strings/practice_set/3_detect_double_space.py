
a = "hello my name  is jayshree  chauhan.Are we  meeting for the  first time?"

#identify double space from string and replace it with single string

while a.find("  ") != -1:
    a = a.replace("  ", " ")


print(a)