from functools import reduce
from fractions import Fraction

def product(fracs):
    t = reduce(lambda x,y : x*y , fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)