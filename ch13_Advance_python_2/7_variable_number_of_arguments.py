
# *args lets your function accept any number of positional arguments (like 1, 2, 3).
# Inside the function, args will be a tuple.

def add_all(*args):
    print(args)
    return sum(args)

print(add_all(1, 2, 3))         # Output: 6
print(add_all(5, 10, 15, 20))   # Output: 50


# **kwargs → Variable Number of Keyword Arguments
# **kwargs lets your function accept any number of keyword arguments (like name="Jayshree").

# Inside the function, kwargs will be a dictionary.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Jayshree", age=28, city="Surat")