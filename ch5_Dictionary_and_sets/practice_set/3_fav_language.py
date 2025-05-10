
d = {} #defined empty dictionary
a = "key"

for i in range(4):
    b = (a + str(i)) #string concatination
    c = input(f"Enter fav language for index {i} : ")
    d.update({b:c})


print(d)