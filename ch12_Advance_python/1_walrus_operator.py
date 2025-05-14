# Without walrus

value =(input("Enter something: "))
if len(value) > 5:
    print("Long input:", value)


# With walrus
if (value := input("Enter something: ")) and len(value) > 5:
    print("Long input:", value)