import time

# decorator is a function that extends the behaviour of the function without modifying the base function
# we pass the base function as an argument to the decorator


def ticktoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f"function({func.__name__}) ran for {round(t2,3)} sec")
    return wrapper




@ticktoc
def work1():
    time.sleep(1.3)

@ticktoc
def work2():
    time.sleep(3)



work1()
work2()
print("-----------------------DONE---------------------")

