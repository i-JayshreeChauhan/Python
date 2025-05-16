
# you have a table of multiplication table of 7 , you need to convert it to a vertial string

table = [str(7*i) for i in range(1,11)]
print(table)

s = "\n".join(table)
print(s)
