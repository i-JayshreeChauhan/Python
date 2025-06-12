cube = lambda x: x**3

l = []  #empty list

def fibonacci(x):
    fib_sequence = []
    a, b = 0, 1
    while a <= x:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
