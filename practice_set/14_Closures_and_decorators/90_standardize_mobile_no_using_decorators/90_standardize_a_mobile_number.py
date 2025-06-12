def wrapper(f):
    def fun(l):
        #need to fetch last 10 digits of all list members
        length = len(l)
        l = [i[-10:] for i in l] #l is now a list of 10 digit number
        for index in range(length):
            num = l[index]
            l[index] = f"+91 {num[:5]} {num[5:]}"
        f(l)
        #wxy
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


