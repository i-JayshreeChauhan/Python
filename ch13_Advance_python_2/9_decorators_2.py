

def add_sprinkles(func):   #decorator function 1
    def wrapper(*args,**kwargs):
        print("**Added sprinklers**")
        func(*args,**kwargs)
    return wrapper

def add_syrup(func):   #decorator function 2
    def wrapper(*args,**kwargs):
        print("**Added Syrup**")
        func(*args,**kwargs)
    return wrapper


@add_syrup
@add_sprinkles
def get_icecream(flavour):
    print(f"Your icecream of {flavour} is ready!")


get_icecream("vanilla")