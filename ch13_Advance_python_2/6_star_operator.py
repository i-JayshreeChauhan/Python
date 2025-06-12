
#example of * operator at the end
data = [10, 20, 30, 40, 50]

a,b, *c = data               # *<variable> collects the remianing data
print(a)  # 10
print(b)  # 20
print(c)  # [30, 40, 50]


#example of * operator in the middle
data = [1, 2, 3, 4, 5]

a, *b, c = data
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


#example of * operator in function arguments
def add_all(*numbers):           # *numbers collects all passed arguments into a tuple.
    return sum(numbers)

print(add_all(1, 2, 3, 4))  # 10


#another example

nums = [2, 3]
print(pow(*nums))  # Same as pow(2, 3), gives 8